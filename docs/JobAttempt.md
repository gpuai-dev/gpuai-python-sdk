# JobAttempt

One run of a job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt** | **int** |  | 
**reservation_mb** | **int** |  | 
**whole_gpu** | **bool** |  | 
**prediction_source** | **str** |  | 
**outcome** | **str** | How the attempt ended. &#x60;oom&#x60; is an out-of-memory exit, &#x60;evicted&#x60; is a stop for outgrowing the reservation on a full GPU, &#x60;lost&#x60; means the machine or the container disappeared, and &#x60;infra&#x60; means the GPU&#39;s sharing layer failed under the job. &#x60;lost&#x60; and &#x60;infra&#x60; do not use a retry. Null while the attempt is in progress.  | 
**reason** | **str** |  | 
**exit_code** | **int** |  | 
**peak_memory_mb** | **int** |  | 
**predicted_compute_pct** | **int** |  | 
**util_mean_pct** | **int** |  | 
**busy_pct** | **int** |  | 
**compute_source** | **str** | How the attempt&#39;s compute profile was attributed. &#x60;process&#x60; is the job&#39;s own per-process utilization, measured even while it shared. &#x60;solo&#x60; uses the GPU&#39;s utilization while the job was alone on it. &#x60;shared_upper_bound&#x60; uses the GPU&#39;s utilization while it shared, which over-states the job&#39;s own.  | 
**memory_source** | **str** |  | 
**sharing_mode** | **str** |  | 
**mig_profile** | **str** | The GPU slice the attempt ran in, or null. | 
**resumed** | **bool** | Whether the attempt started with files already in its checkpoint directory. | 
**started_at** | **datetime** |  | 
**ended_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.job_attempt import JobAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of JobAttempt from a JSON string
job_attempt_instance = JobAttempt.from_json(json)
# print the JSON string representation of the object
print(JobAttempt.to_json())

# convert the object into a dict
job_attempt_dict = job_attempt_instance.to_dict()
# create an instance of JobAttempt from a dict
job_attempt_from_dict = JobAttempt.from_dict(job_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


