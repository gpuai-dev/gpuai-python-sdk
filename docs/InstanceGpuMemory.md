# InstanceGpuMemory

The highest GPU memory use seen on an instance since launch, from the telemetry every instance reports about every two minutes. On an instance with several GPUs it is the busiest GPU. Absent on an instance until its first sample arrives. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peak_used_mb** | **int** | Highest memory in use on the GPU, in MiB. | 
**total_mb** | **int** | The GPU&#39;s total memory, in MiB. | 
**samples** | **int** | How many telemetry samples the peak is taken from. | 
**last_sample_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.instance_gpu_memory import InstanceGpuMemory

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceGpuMemory from a JSON string
instance_gpu_memory_instance = InstanceGpuMemory.from_json(json)
# print the JSON string representation of the object
print(InstanceGpuMemory.to_json())

# convert the object into a dict
instance_gpu_memory_dict = instance_gpu_memory_instance.to_dict()
# create an instance of InstanceGpuMemory from a dict
instance_gpu_memory_from_dict = InstanceGpuMemory.from_dict(instance_gpu_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


