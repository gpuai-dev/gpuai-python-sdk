# JobGpuTypesDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** | The GPU model, as &#x60;gpu_type&#x60; in &#x60;POST /jobs&#x60;. | 
**vram_gb** | **int** | The GPU&#39;s memory in GB. | 
**available_now** | **bool** | True when a supplier that runs jobs had a one-GPU machine of this type to rent at the last catalog read, a few minutes ago, and recent launches of it were not refused. When &#x60;capacity_checked&#x60; is true, a job for a type that is not available now is refused unless it sets &#x60;wait_for_capacity&#x60;.  | 
**price_per_gpu_hour** | **float** | Cheapest retail price in USD per GPU-hour of such a machine at that read. Null when not available now.  | 
**last_seen_at** | **datetime** | When a supplier that runs jobs last listed the type. | 

## Example

```python
from gpuai_sdk.models.job_gpu_types_data_inner import JobGpuTypesDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of JobGpuTypesDataInner from a JSON string
job_gpu_types_data_inner_instance = JobGpuTypesDataInner.from_json(json)
# print the JSON string representation of the object
print(JobGpuTypesDataInner.to_json())

# convert the object into a dict
job_gpu_types_data_inner_dict = job_gpu_types_data_inner_instance.to_dict()
# create an instance of JobGpuTypesDataInner from a dict
job_gpu_types_data_inner_from_dict = JobGpuTypesDataInner.from_dict(job_gpu_types_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


