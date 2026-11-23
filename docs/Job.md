# Job

A batch job. It names no machine: the machines a job runs on are instances of your organization and appear in the instance list. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**image** | **str** |  | 
**command** | **List[str]** |  | 
**env_names** | **List[str]** | The names of the job&#39;s environment variables. Values are never returned. | 
**secrets** | **List[str]** | Names of the organization secrets the job receives. Empty when none. | 
**gpu_type** | **str** | The requested GPU model, or an empty string when the job asked for &#x60;min_vram_gb&#x60; only. | 
**min_vram_gb** | **int** |  | 
**memory_hint_mb** | **int** |  | 
**compute_hint_pct** | **int** |  | 
**timeout_seconds** | **int** |  | 
**max_wait_seconds** | **int** |  | 
**allow_sharing** | **bool** |  | 
**allow_restart** | **bool** |  | 
**isolation** | **str** |  | 
**mig_profile** | **str** | The GPU slice (NVIDIA MIG profile) a job with &#x60;isolation&#x60; &#x60;hard&#x60; runs in during its current or last attempt, such as &#x60;3g.40gb&#x60;; null for a soft job or one with a whole GPU.  | 
**checkpoint_path** | **str** |  | 
**max_retries** | **int** |  | 
**max_price_per_hour** | **float** |  | 
**trial_funded** | **bool** | The job was submitted with no balance and runs on the free trial. It stops when the trial credit is used.  | [optional] 
**wait_for_capacity** | **bool** | The job was submitted with &#x60;wait_for_capacity&#x60;: it waits for a machine of its type for up to 24 hours instead of being refused or failed for lack of capacity.  | [optional] 
**status** | **str** | &#x60;queued&#x60; is waiting for a GPU, &#x60;assigned&#x60; has a GPU and is about to start, &#x60;running&#x60; is running. &#x60;succeeded&#x60;, &#x60;failed&#x60; and &#x60;cancelled&#x60; are final. A job that is retried goes back to &#x60;queued&#x60;.  | 
**status_reason** | **str** | Why the job is waiting, or why it failed or was retried. | 
**cancel_requested** | **bool** | True once a cancel has been asked for and until the job stops. | 
**attempt** | **int** | The number of the current or last attempt. 0 before the job is first placed. | 
**retries** | **int** | Reruns after a memory failure, counted against &#x60;max_retries&#x60;. | 
**evictions** | **int** | Times the job was stopped for outgrowing its reservation on a full GPU. | 
**oom_exits** | **int** | Times the job exited out of GPU memory. | 
**reservation_mb** | **int** | GPU memory reserved for the current or last attempt, in MiB. For a whole GPU it is the GPU&#39;s total memory. It is used for placement and is not a hard cap.  | 
**whole_gpu** | **bool** | Whether the current or last attempt has a GPU to itself. Null before the job is first placed. | 
**predicted_mb** | **int** | The estimate behind the reservation, from the hint or from history, with headroom. | 
**prediction_source** | **str** | Where the reservation came from: &#x60;hint&#x60;, &#x60;history:org+name&#x60;, &#x60;history:org+image&#x60;, &#x60;history:image&#x60;, &#x60;none&#x60; (no hint and no usable history), &#x60;not_shared&#x60; (the job did not opt in to sharing) or &#x60;no_restart&#x60; (sharing needs restart). &#x60;+retry&#x60; is appended once a memory failure has grown the reservation.  | 
**predicted_compute_pct** | **int** | The compute duty the current or last attempt was charged on its GPU, 1 to 100. 100 when the job&#39;s compute is unknown.  | 
**compute_prediction_source** | **str** | Where the compute duty came from: &#x60;hint&#x60;, &#x60;history:org+name&#x60;, &#x60;history:org+image&#x60;, &#x60;history:image&#x60; or &#x60;none&#x60; (unknown, counted as 100).  | 
**peak_memory_mb** | **int** | The job&#39;s highest GPU memory use so far, across attempts, in MiB. | 
**gpu_memory_total_mb** | **int** | Total memory of the GPU the current or last attempt runs on, in MiB. | 
**util_mean_pct** | **int** | Mean GPU utilization measured during the last finished attempt. See &#x60;compute_source&#x60; on the attempt for how it was attributed.  | 
**busy_pct** | **int** | Share of the last finished attempt&#39;s samples with GPU utilization at or above 50%. Close to &#x60;util_mean_pct&#x60; for a job that runs in on/off bursts, near 0 or 100 for a steady one.  | 
**memory_source** | **str** | Where the job&#39;s memory numbers come from: &#x60;process&#x60; is the GPU&#39;s per-process accounting, &#x60;limit&#x60; means per-process memory was not visible and the reservation stands in for it.  | 
**sharing_mode** | **str** | How the GPU was shared during the last attempt. &#x60;mig&#x60; is a GPU slice of the job&#39;s own. | 
**gpu_seconds** | **float** | Seconds the job has spent running on a GPU, across attempts. | 
**attributed_cost_usd** | **float** | The job&#39;s share of its machines&#39; price, for display. A GPU&#39;s hourly price is split equally between the jobs running on it at the time, so a job that shared a GPU is attributed less than one that had it alone. A job in a GPU slice is attributed its slice&#39;s share of the GPU (for example 3/7 for &#x60;3g.40gb&#x60;). Machine time with no job running is not attributed to any job. The bill of record is the machine&#39;s instance billing.  | 
**exit_code** | **int** |  | 
**created_at** | **datetime** |  | 
**started_at** | **datetime** | When the current or last attempt started. | 
**finished_at** | **datetime** |  | 
**sharing_hint** | [**JobSharingHint**](JobSharingHint.md) |  | [optional] 
**attempts** | [**List[JobAttempt]**](JobAttempt.md) | The job&#39;s attempts, oldest first. Returned by GET /v1/jobs/{id} only. | [optional] 

## Example

```python
from gpuai_sdk.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


