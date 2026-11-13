# GpuSuggestionGpu

A GPU model at an hourly price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** | The GPU model id, as in GET /v1/gpu-types. | 
**gpu_name** | **str** | The GPU model&#39;s display name. | 
**vram_gb** | **int** | Memory per GPU, in GB. | 
**price_per_hour** | **float** | Hourly price for the same number of GPUs as the instance. | 

## Example

```python
from gpuai_sdk.models.gpu_suggestion_gpu import GpuSuggestionGpu

# TODO update the JSON string below
json = "{}"
# create an instance of GpuSuggestionGpu from a JSON string
gpu_suggestion_gpu_instance = GpuSuggestionGpu.from_json(json)
# print the JSON string representation of the object
print(GpuSuggestionGpu.to_json())

# convert the object into a dict
gpu_suggestion_gpu_dict = gpu_suggestion_gpu_instance.to_dict()
# create an instance of GpuSuggestionGpu from a dict
gpu_suggestion_gpu_from_dict = GpuSuggestionGpu.from_dict(gpu_suggestion_gpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


