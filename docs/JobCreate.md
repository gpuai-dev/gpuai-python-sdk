# JobCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A label for the job. Jobs whose names match once digits are removed (&#x60;train-run-17&#x60;, &#x60;train-run-18&#x60;) are treated as repeats of the same work, and the peak memory of earlier finished runs is used to size later ones. Naming repeat jobs consistently is the simplest way to have them share a GPU without a memory hint.  | [optional] 
**image** | **str** | The container image to run, such as &#x60;registry.example.com/team/train:1.2&#x60;. The machine must be able to pull it without credentials.  | 
**command** | **List[str]** | The program and its arguments. The first item replaces the image&#39;s entrypoint and the rest are its arguments, so &#x60;[\&quot;python\&quot;, \&quot;train.py\&quot;, \&quot;--epochs\&quot;, \&quot;3\&quot;]&#x60; runs exactly that.  | 
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
**secrets** | **List[str]** | Names of organization secrets (POST /secrets) the job&#39;s container receives as environment variables of the same names. Values are never in a response or a log. Returns 422 &#x60;validation_failed&#x60; when a name does not exist or secrets are not enabled on this deployment. | [optional] 

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


