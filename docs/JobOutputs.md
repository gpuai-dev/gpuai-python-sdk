# JobOutputs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** | What the status means for this job, in plain words. | 
**outputs_path** | **str** | The directory in the container that is uploaded. | 
**filename** | **str** |  | [optional] 
**bytes** | **int** | Size of the zip archive. | [optional] 
**files** | [**List[JobOutputFile]**](JobOutputFile.md) | The files in the archive, at most 200 listed. | 
**attempt** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**url** | **str** | Downloads the zip archive until url_expires_at. | [optional] 
**url_expires_at** | **datetime** |  | [optional] 
**max_bytes** | **int** | The most one job&#39;s outputs may hold. | 

## Example

```python
from gpuai_sdk.models.job_outputs import JobOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of JobOutputs from a JSON string
job_outputs_instance = JobOutputs.from_json(json)
# print the JSON string representation of the object
print(JobOutputs.to_json())

# convert the object into a dict
job_outputs_dict = job_outputs_instance.to_dict()
# create an instance of JobOutputs from a dict
job_outputs_from_dict = JobOutputs.from_dict(job_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


