"""Find imports a function's pip list will not install, before any machine starts.

A function runs on a machine that has only its ``pip`` list installed, so an
import missing from that list fails the call after a paid cold start. This
module reads the function's code (no code is run) and reports a module only
when this computer's installed package metadata shows that no listed
requirement installs it. When that cannot be shown (a requirement is not
installed here, or is a URL), it reports nothing: a warning that may be wrong
costs the user more time than it saves.

It cannot see imports made by the packages themselves (a package that imports
another without declaring it); those surface on the machine as a
ModuleNotFoundError whose message names the package to add.
"""

from __future__ import annotations

import dis
import importlib.util
import re
import sys
import types
from importlib import metadata
from typing import Callable, Dict, Iterable, List, Optional, Set

# Import names whose pip package is spelled differently. Kept in step with
# MODULE_TO_PACKAGE in the runner (internal/functions/runner/runner.py).
MODULE_TO_PACKAGE = {
    "PIL": "pillow",
    "cv2": "opencv-python-headless",
    "sklearn": "scikit-learn",
    "skimage": "scikit-image",
    "yaml": "pyyaml",
    "bs4": "beautifulsoup4",
    "dateutil": "python-dateutil",
    "dotenv": "python-dotenv",
    "jwt": "pyjwt",
    "Crypto": "pycryptodome",
    "attr": "attrs",
    "fitz": "pymupdf",
    "docx": "python-docx",
    "pptx": "python-pptx",
    "zmq": "pyzmq",
    "OpenSSL": "pyopenssl",
    "Levenshtein": "levenshtein",
    "flash_attn": "flash-attn",
    "llama_cpp": "llama-cpp-python",
    "mpl_toolkits": "matplotlib",
    "git": "gitpython",
    "websocket": "websocket-client",
    "pytorch_lightning": "pytorch-lightning",
    "imageio_ffmpeg": "imageio-ffmpeg",
}

# Pip names that provide an import name besides the one in MODULE_TO_PACKAGE
# (any of these in pip covers the import).
_ALTERNATIVES = {
    "cv2": {"opencv-python", "opencv-python-headless", "opencv-contrib-python", "opencv-contrib-python-headless"},
}

_REQ_NAME = re.compile(r"^\s*([A-Za-z0-9][A-Za-z0-9._-]*)\s*(\[[^\]]*\])?")


class MissingPackageWarning(UserWarning):
    """A function imports a module its ``pip`` list does not install."""


def normalize(name: str) -> str:
    """PEP 503 normalized distribution name."""
    return re.sub(r"[-_.]+", "-", name).lower()


def requirement_name(req: str) -> Optional[str]:
    """The distribution a pip requirement names, or None for a URL or path."""
    req = req.strip()
    if "://" in req.split("@", 1)[0] or req.startswith((".", "/")):
        return None
    m = _REQ_NAME.match(req)
    return normalize(m.group(1)) if m else None


def imported_modules(fn: Callable, shipped: Iterable[types.ModuleType] = ()) -> Set[str]:
    """Top-level module names the function needs on the machine.

    Two kinds: ``import`` statements anywhere in its code (nested functions,
    comprehensions and lambdas included), and modules its code names as
    globals, which the pickle imports when it is loaded. Functions from
    shipped modules travel by value, so their code is read too.
    """
    shipped_names = {m.__name__ for m in shipped if isinstance(m, types.ModuleType)}
    found: Set[str] = set()
    seen_code: Set[int] = set()
    seen_fn: Set[int] = set()

    def visit_function(f: Callable) -> None:
        f = getattr(f, "__wrapped__", f)
        code = getattr(f, "__code__", None)
        if code is None or id(f) in seen_fn:
            return
        seen_fn.add(id(f))
        # Names the code reads: its globals, and the variables it closes over
        # (a module imported in an enclosing function).
        names: Dict[str, object] = dict(getattr(f, "__globals__", {}) or {})
        for var, cell in zip(code.co_freevars, getattr(f, "__closure__", None) or ()):
            try:
                names[var] = cell.cell_contents
            except ValueError:
                pass  # an empty cell
        visit_code(code, names)

    def visit_code(code: types.CodeType, globs: Dict[str, object]) -> None:
        if id(code) in seen_code:
            return
        seen_code.add(id(code))
        window: List[dis.Instruction] = []  # the two instructions before this one
        for ins in dis.get_instructions(code):
            if ins.opname == "IMPORT_NAME" and isinstance(ins.argval, str) and ins.argval:
                # IMPORT_NAME follows LOAD_CONST level, LOAD_CONST fromlist. A
                # relative import (level > 0) is the shipped module's own.
                level = window[0].argval if len(window) == 2 and isinstance(window[0].argval, int) else 0
                if level == 0:
                    found.add(ins.argval.split(".")[0])
            window = (window + [ins])[-2:]
        for name in code.co_names + code.co_freevars:
            value = globs.get(name)
            if isinstance(value, types.ModuleType):
                found.add(value.__name__.split(".")[0])
            elif isinstance(value, types.FunctionType) and getattr(value, "__module__", None) in shipped_names:
                visit_function(value)
        for const in code.co_consts:
            if isinstance(const, types.CodeType):
                visit_code(const, globs)

    visit_function(fn)
    return found


def _requires(dist: str) -> Optional[List[str]]:
    """Distributions dist depends on (every extra and marker included, so the
    closure only ever over-covers), or None when dist is not installed here."""
    try:
        reqs = metadata.requires(dist) or []
    except metadata.PackageNotFoundError:
        return None
    out = []
    for r in reqs:
        name = requirement_name(r.split(";", 1)[0])
        if name:
            out.append(name)
    return out


def _closure(roots: Iterable[str]):
    """(every distribution the roots install, whether all of them are
    installed here) from local metadata; None when a root itself is not
    installed on this computer (then nothing can be shown)."""
    seen: Set[str] = set()
    complete = True
    todo = list(roots)
    roots = set(todo)
    while todo:
        dist = todo.pop()
        if dist in seen:
            continue
        seen.add(dist)
        deps = _requires(dist)
        if deps is None:
            if dist in roots:
                return None
            complete = False  # a dependency not installed here; it may provide anything
            continue
        todo.extend(deps)
    return seen, complete


def _local_origin(mod: str) -> Optional[str]:
    """Where this computer would import mod from, without importing it."""
    try:
        spec = importlib.util.find_spec(mod)
    except (ImportError, ValueError):
        return None
    if spec is None:
        return None
    return spec.origin or (list(spec.submodule_search_locations or []) or [None])[0]


def find_missing(
    fn: Callable,
    pip: Iterable[str],
    python_version: str,
    shipped: Iterable[types.ModuleType] = (),
) -> List[str]:
    """Warnings, one per module the function imports that will not be on the
    machine. Empty when everything is covered or nothing can be shown."""
    # Python 3.10 functions run in an environment that also sees the machine
    # image's own packages, which this computer cannot list.
    if python_version == "3.10":
        return []
    pip = list(pip)
    names = [requirement_name(r) for r in pip]
    if any(n is None for n in names):
        return []
    found = _closure({n for n in names if n})
    if found is None:
        return []
    closure, complete = found
    shipped = list(shipped)
    shipped_tops = {m.__name__.split(".")[0] for m in shipped if isinstance(m, types.ModuleType)}
    stdlib = set(sys.stdlib_module_names) | set(sys.builtin_module_names)
    providers = metadata.packages_distributions()
    listed = ", ".join(repr(p) for p in pip)
    name = getattr(fn, "__name__", "the function")
    out = []
    for mod in sorted(imported_modules(fn, shipped)):
        if mod in stdlib or mod in shipped_tops or mod in ("__main__", "cloudpickle") or mod.startswith("_"):
            continue
        local_dists = {normalize(d) for d in providers.get(mod, [])}
        package = MODULE_TO_PACKAGE.get(mod) or (sorted(providers[mod])[0] if providers.get(mod) else mod.replace("_", "-"))
        candidates = local_dists | {normalize(mod), normalize(package)} | _ALTERNATIVES.get(mod, set())
        if candidates & closure:
            continue
        if not local_dists:
            origin = _local_origin(mod)
            if origin and "-packages" not in origin.replace("\\", "/"):
                out.append(
                    f"{name} imports {mod}, a module from your own files ({origin}) that is not shipped with it, so "
                    f"the call would fail on the machine with ModuleNotFoundError. Pass include=[{mod}] to @function."
                )
                continue
            if not complete or origin:
                # A dependency this computer does not have may provide it.
                continue
        out.append(
            f"{name} imports {mod}, but pip=[{listed}] does not install it (checked against the packages installed "
            f"on this computer), so the call would fail on the machine with ModuleNotFoundError. "
            f'Add "{package}" to pip=[...].'
        )
    return out
