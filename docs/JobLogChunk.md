# JobLogChunk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**attempt** | **int** |  | 
**text** | **str** | A piece of the job&#39;s combined output, at most 16 KB. | 
**created_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.job_log_chunk import JobLogChunk

# TODO update the JSON string below
json = "{}"
# create an instance of JobLogChunk from a JSON string
job_log_chunk_instance = JobLogChunk.from_json(json)
# print the JSON string representation of the object
print(JobLogChunk.to_json())

# convert the object into a dict
job_log_chunk_dict = job_log_chunk_instance.to_dict()
# create an instance of JobLogChunk from a dict
job_log_chunk_from_dict = JobLogChunk.from_dict(job_log_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


