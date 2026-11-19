# JobSharingHint

Advisory only, and present only when it applies. A job carries it when it succeeded with a whole GPU it did not allow to be shared, ran at least a minute with no out-of-memory exit or eviction, and its peak GPU memory, measured from per-process accounting (`memory_source` `process`), was at most half of the GPU's memory. Sharing stays opt-in; the hint never changes how a job is placed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A short sentence to show the user, such as \&quot;This job used 5.1 GB of its 48 GB GPU. Set allow_sharing and allow_restart to true to let it share a GPU with your other jobs and pay only for its share.\&quot; It names only the flags the job did not already set.  | 
**peak_memory_mb** | **int** | The job&#39;s measured peak GPU memory, in MiB. | 
**gpu_memory_total_mb** | **int** | Total memory of the GPU the job held, in MiB. | 

## Example

```python
from gpuai_sdk.models.job_sharing_hint import JobSharingHint

# TODO update the JSON string below
json = "{}"
# create an instance of JobSharingHint from a JSON string
job_sharing_hint_instance = JobSharingHint.from_json(json)
# print the JSON string representation of the object
print(JobSharingHint.to_json())

# convert the object into a dict
job_sharing_hint_dict = job_sharing_hint_instance.to_dict()
# create an instance of JobSharingHint from a dict
job_sharing_hint_from_dict = JobSharingHint.from_dict(job_sharing_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


