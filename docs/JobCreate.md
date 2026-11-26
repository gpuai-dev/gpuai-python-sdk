# JobCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A label for the job. Jobs whose names match once digits are removed (&#x60;train-run-17&#x60;, &#x60;train-run-18&#x60;) are treated as repeats of the same work, and the peak memory of earlier finished runs is used to size later ones. Naming repeat jobs consistently is the simplest way to have them share a GPU without a memory hint.  | [optional] 
**image** | **str** | The container image to run, such as &#x60;registry.example.com/team/train:1.2&#x60;. The machine must be able to pull it without credentials. Required unless the deployment runs a default image: then it may be left out, &#x60;gpu_type&#x60; is required, and the job runs on the GPU.ai PyTorch image built for that GPU.  | [optional] 
**command** | **List[str]** | The program and its arguments. The first item replaces the image&#39;s entrypoint and the rest are its arguments, so &#x60;[\&quot;python\&quot;, \&quot;train.py\&quot;, \&quot;--epochs\&quot;, \&quot;3\&quot;]&#x60; runs exactly that. Send this or &#x60;script&#x60;.  | [optional] 
**script** | **str** | A shell script run with &#x60;bash -c&#x60; in place of &#x60;command&#x60;, such as &#x60;pip install -r requirements.txt &amp;&amp; python train.py&#x60;. Only where the deployment runs a default image; elsewhere it is refused with a 422.  | [optional] 
**repo** | [**JobCreateRepo**](JobCreateRepo.md) |  | [optional] 
**env** | **Dict[str, str]** | Environment variables for the job, at most 100. Names starting with &#x60;GPUAI_&#x60; are reserved. Values are stored to run the job and are never returned by the API.  | [optional] 
**gpu_type** | **str** | The GPU model to run on, as in GET /v1/gpu-types. One of &#x60;gpu_type&#x60; or &#x60;min_vram_gb&#x60; is required.  | [optional] 
**min_vram_gb** | **int** | Run on any GPU model with at least this much memory, in GB. Used when &#x60;gpu_type&#x60; is not given.  | [optional] 
**memory_hint_mb** | **int** | The peak GPU memory you expect the job to use, in MiB. The reservation is the hint plus headroom (15% and 512 MiB). Without a hint the platform uses the history of earlier finished jobs, and a job with neither gets a whole GPU.  | [optional] 
**compute_hint_pct** | **int** | The share of time you expect the job to keep the GPU busy, 1 to 100. Jobs share a GPU only while the sum of their compute duties stays at or under 100. Without a hint the platform uses the measured utilization of earlier finished jobs with the same name or image, and a job with neither counts as 100 (a GPU to itself).  | [optional] 
**timeout_seconds** | **int** | The job is stopped and fails after running this long. | [optional] [default to 3600]
**max_wait_seconds** | **int** | Opt in to waiting. When no machine in your pool has room, wait up to this long for space before starting a new machine. 0 starts a machine at once.  | [optional] [default to 0]
**allow_sharing** | **bool** | Opt in to sharing. The job may run on the same GPU as other jobs from your own organization that also opted in. Needs &#x60;allow_restart&#x60;, and a memory hint or usable history; otherwise the job still gets a whole GPU. A GPU is never shared with another customer.  | [optional] [default to False]
**allow_restart** | **bool** | Opt in to restart. The platform may stop the job and run it again: after it runs out of GPU memory, after it outgrows its reservation on a full GPU, or after its machine is lost. Use the checkpoint directory to resume instead of starting over.  | [optional] [default to False]
**isolation** | **str** | &#x60;soft&#x60; (the default) is the sharing described under &#x60;allow_sharing&#x60;. &#x60;hard&#x60; runs the job in a GPU slice of its own (NVIDIA MIG): its own memory, its own compute and its own fault domain, so another job on the same GPU cannot slow it down, take its memory or crash it. The slice is the smallest that holds the memory hint or the job&#39;s history; without either, or when no slice is large enough, the job gets a whole GPU. A slice has a share of the GPU&#39;s compute in proportion to its size, so a job in a small slice runs slower than on a whole GPU. Needs &#x60;gpu_type&#x60; set to a model that supports slices (&#x60;a100_80gb&#x60; or &#x60;h100_pcie&#x60;), and cannot be combined with &#x60;allow_sharing&#x60;. Not available until enabled for your organization.  | [optional] [default to 'soft']
**checkpoint_path** | **str** | Where the job&#39;s checkpoint directory is mounted inside the container. Defaults to &#x60;/gpuai/checkpoint&#x60;. The same path is in the &#x60;GPUAI_CHECKPOINT_DIR&#x60; environment variable. Files written there are still present when the job is run again on the same machine. They do not follow the job to another machine.  | [optional] 
**max_retries** | **int** | How many times to rerun the job after it runs out of GPU memory or is stopped for outgrowing its reservation. Defaults to 2. Other failures are never retried.  | [optional] 
**max_price_per_hour** | **float** | Only run on a machine whose hourly price is at most this. Machines are launched on the cheapest suitable listing in any region.  | [optional] 
**wait_for_capacity** | **bool** | Queue the job even when no machine of its GPU type is available right now (&#x60;available_now&#x60; false in &#x60;GET /jobs/gpu-types&#x60;), and keep it waiting for one for up to 24 hours. Without it such a job is refused with 422 and the nearest type that is available, and a queued job whose machine launches keep being refused for lack of capacity fails within a few minutes.  | [optional] [default to False]
**secrets** | **List[str]** | Names of organization secrets (POST /secrets) the job&#39;s container receives as environment variables of the same names. Values are never in a response or a log. Returns 422 &#x60;validation_failed&#x60; when a name does not exist or secrets are not enabled on this deployment. | [optional] 
**input_file** | **str** | The id of a file uploaded with POST /jobs/inputs. When the job starts it gets a short-lived URL of the file in &#x60;GPUAI_INPUT_URL&#x60; and its name in &#x60;GPUAI_INPUT_NAME&#x60;. A file is read by one job only. Returns 422 &#x60;validation_failed&#x60; when the file was not uploaded, has expired, is already used, or job files are not enabled on this deployment. | [optional] 
**env_from_job** | **str** | The id of an earlier job of yours whose environment variables this job starts with. Variables in &#x60;env&#x60; are applied over them. Use it to resubmit an edited job without sending its values again: the API never returns env values. Returns 422 &#x60;validation_failed&#x60; when no such job of your organization exists. | [optional] 

## Example

```python
from gpuai_sdk.models.job_create import JobCreate

# TODO update the JSON string below
json = "{}"
# create an instance of JobCreate from a JSON string
job_create_instance = JobCreate.from_json(json)
# print the JSON string representation of the object
print(JobCreate.to_json())

# convert the object into a dict
job_create_dict = job_create_instance.to_dict()
# create an instance of JobCreate from a dict
job_create_from_dict = JobCreate.from_dict(job_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


