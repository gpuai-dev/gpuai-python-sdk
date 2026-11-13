# GpuSuggestionCheaper

The suggested GPU model and what it would save.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** |  | 
**gpu_name** | **str** |  | 
**vram_gb** | **int** |  | 
**price_per_hour** | **float** | The cheapest current listing for this model, per hour. | 
**saving_per_hour** | **float** | The instance&#39;s hourly price minus this model&#39;s. | 
**saving_pct** | **float** | The saving as a percentage of the instance&#39;s hourly price. | 

## Example

```python
from gpuai_sdk.models.gpu_suggestion_cheaper import GpuSuggestionCheaper

# TODO update the JSON string below
json = "{}"
# create an instance of GpuSuggestionCheaper from a JSON string
gpu_suggestion_cheaper_instance = GpuSuggestionCheaper.from_json(json)
# print the JSON string representation of the object
print(GpuSuggestionCheaper.to_json())

# convert the object into a dict
gpu_suggestion_cheaper_dict = gpu_suggestion_cheaper_instance.to_dict()
# create an instance of GpuSuggestionCheaper from a dict
gpu_suggestion_cheaper_from_dict = GpuSuggestionCheaper.from_dict(gpu_suggestion_cheaper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


