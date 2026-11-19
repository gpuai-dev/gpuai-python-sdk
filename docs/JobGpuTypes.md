# JobGpuTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JobGpuTypesDataInner]**](JobGpuTypesDataInner.md) |  | 
**complete** | **bool** | True when the list is authoritative and any other gpu_type is refused at submit. | 

## Example

```python
from gpuai_sdk.models.job_gpu_types import JobGpuTypes

# TODO update the JSON string below
json = "{}"
# create an instance of JobGpuTypes from a JSON string
job_gpu_types_instance = JobGpuTypes.from_json(json)
# print the JSON string representation of the object
print(JobGpuTypes.to_json())

# convert the object into a dict
job_gpu_types_dict = job_gpu_types_instance.to_dict()
# create an instance of JobGpuTypes from a dict
job_gpu_types_from_dict = JobGpuTypes.from_dict(job_gpu_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


