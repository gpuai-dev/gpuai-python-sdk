# JobLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JobLogChunk]**](JobLogChunk.md) |  | 
**next_after** | **int** | Pass this as &#x60;after&#x60; to read on from here. | 

## Example

```python
from gpuai_sdk.models.job_logs import JobLogs

# TODO update the JSON string below
json = "{}"
# create an instance of JobLogs from a JSON string
job_logs_instance = JobLogs.from_json(json)
# print the JSON string representation of the object
print(JobLogs.to_json())

# convert the object into a dict
job_logs_dict = job_logs_instance.to_dict()
# create an instance of JobLogs from a dict
job_logs_from_dict = JobLogs.from_dict(job_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


