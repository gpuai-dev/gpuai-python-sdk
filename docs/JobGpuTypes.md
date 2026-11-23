# JobGpuTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JobGpuTypesDataInner]**](JobGpuTypesDataInner.md) |  | 
**complete** | **bool** | True when the list is authoritative and any other gpu_type is refused at submit. | 
**capacity_checked** | **bool** | True when &#x60;available_now&#x60; is a live answer that submit acts on: a job for a type that is not available now (or, with only &#x60;min_vram_gb&#x60;, when no available type is that large) is refused with 422 unless it sets &#x60;wait_for_capacity&#x60;. False when the stock could not be read just now: nothing is then refused for capacity.  | [optional] 

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


