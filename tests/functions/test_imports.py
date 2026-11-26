"""The deploy-time import check: report imports the machine will not have,
before any machine starts, and never report one that will be there."""

import os
import sys
import warnings

import pytest
import urllib3  # installed with the SDK; no requirement used below depends on it

from gpuai_sdk.functions import MissingPackageWarning, function
from gpuai_sdk.functions._imports import find_missing, imported_modules, requirement_name

PY = "3.12"


def check(fn, pip, py=PY, shipped=()):
    return find_missing(fn, pip, py, shipped)


def test_imports_in_the_body_nested_code_and_module_globals_are_found():
    def f():
        import json  # noqa: F401
        import dateutil.parser  # noqa: F401

        def inner():
            from PIL import Image  # noqa: F401

        return [urllib3 for _ in range(1)], (lambda: __import__("x"))

    assert {"json", "dateutil", "PIL", "urllib3"} <= imported_modules(f)


def test_a_module_the_pip_list_installs_directly_or_transitively_is_quiet():
    def f():
        import dateutil  # provided by python-dateutil

        return dateutil

    def g():
        import pluggy  # noqa: F401  (a dependency of pytest)
        import iniconfig  # noqa: F401  (another one)

    assert check(f, ["python-dateutil>=2.8"]) == []
    assert check(f, ["python_dateutil"]) == []
    assert check(g, ["pytest"]) == []


def test_a_module_no_requirement_installs_is_reported_with_the_package_to_add():
    def f():
        return urllib3.__version__

    [msg] = check(f, ["python-dateutil"])
    assert "f imports urllib3" in msg and 'Add "urllib3" to pip=[...]' in msg
    assert "ModuleNotFoundError" in msg


def test_an_empty_pip_list_reports_every_third_party_import_with_known_names():
    def f():
        import os  # noqa: F401  (standard library)
        import torch  # noqa: F401
        from PIL import Image  # noqa: F401
        import cv2  # noqa: F401

    msgs = "\n".join(check(f, []))
    assert 'imports torch' in msgs and 'Add "torch"' in msgs
    assert 'Add "pillow"' in msgs and 'Add "opencv-python-headless"' in msgs
    assert "imports os" not in msgs


def test_nothing_is_reported_when_it_cannot_be_shown():
    def f():
        import torch  # noqa: F401
        return urllib3

    # A requirement this computer does not have installed: its dependencies
    # are unknown, so it might install anything.
    assert check(f, ["diffsynth-not-installed-here==2.0.11"]) == []
    # A URL requirement.
    assert check(f, ["https://example.com/pkg.whl"]) == []
    # Python 3.10 functions also see the machine image's packages.
    assert check(f, [], py="3.10") == []


def test_opencv_variants_all_cover_cv2(monkeypatch):
    import gpuai_sdk.functions._imports as imp

    monkeypatch.setattr(imp, "_closure", lambda roots: (set(roots), True))

    def f():
        import cv2  # noqa: F401

    for pkg in ("opencv-python", "opencv-python-headless", "opencv-contrib-python"):
        assert check(f, [pkg]) == [], pkg


def test_a_local_module_that_is_not_shipped_is_reported_with_include(tmp_path, monkeypatch):
    (tmp_path / "my_helpers_zz.py").write_text("def prep(x):\n    return x\n")
    monkeypatch.syspath_prepend(str(tmp_path))
    import my_helpers_zz

    def f(x):
        return my_helpers_zz.prep(x)

    [msg] = check(f, [])
    assert "imports my_helpers_zz, a module from your own files" in msg and "include=[my_helpers_zz]" in msg
    assert check(f, [], shipped=[my_helpers_zz]) == []


def test_requirement_names():
    assert requirement_name("transformers>=4.51,<5") == "transformers"
    assert requirement_name("Diff_Synth[extra]==2.0") == "diff-synth"
    assert requirement_name("pkg @ https://x/y.whl") == "pkg"
    assert requirement_name("https://x/y.whl") is None
    assert requirement_name("./local") is None


@pytest.fixture()
def fake_api(monkeypatch):
    from test_functions import FakeAPI
    import gpuai_sdk.functions as fn_lib

    fake = FakeAPI()
    monkeypatch.setenv("GPUAI_API_KEY", "test-key")
    monkeypatch.setenv("GPUAI_API_BASE", fake.base)
    monkeypatch.setattr(fn_lib._client, "_config", {"api_key": None, "api_base": None})
    yield fake
    fake.server.shutdown()


def test_deploy_warns_before_any_machine_starts_and_still_deploys(fake_api):
    @function(pip=["python-dateutil"], name="imports_check")
    def f():
        return urllib3.__version__

    assert f.check_imports() and "urllib3" in f.check_imports()[0]
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        f.deploy()
    assert [w for w in caught if issubclass(w.category, MissingPackageWarning)]
    assert fake_api.count("POST", "/versions") == 1  # a warning, never a block
    assert fake_api.count("POST", "/runs") == 0


def test_a_covered_function_deploys_without_a_warning(fake_api):
    @function(pip=["urllib3"], name="imports_ok")
    def f():
        return urllib3.__version__

    with warnings.catch_warnings():
        warnings.simplefilter("error", MissingPackageWarning)
        f.deploy()


def test_relative_imports_are_the_shipped_modules_own():
    src = "def f():\n    from . import sibling\n    from .pkg import thing\n    import absolute_zz\n"
    ns = {"__name__": "mypkg.mod", "__package__": "mypkg"}
    exec(compile(src, "<mod>", "exec"), ns)
    assert imported_modules(ns["f"]) == {"absolute_zz"}
