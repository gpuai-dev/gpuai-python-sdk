# GpuSuggestion

Whether a lower-priced GPU model would have fit an instance's observed peak GPU memory. It names GPU models and prices only. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | &#x60;suggestion&#x60; when a cheaper model fits and the saving is at least 10% and $0.05 per hour. &#x60;insufficient_data&#x60; until the instance has at least 30 samples over at least an hour. &#x60;no_cheaper_fit&#x60; otherwise.  | 
**peak_used_mb** | **int** | Highest GPU memory seen, in MiB. Null with no telemetry. | 
**required_mb** | **int** | The peak plus headroom (25% and 1024 MiB), in MiB: the memory a suggested model must have. Null until there is enough telemetry.  | 
**samples** | **int** |  | 
**observed_minutes** | **int** | Minutes between the first and the latest telemetry sample. | 
**current** | [**GpuSuggestionGpu**](GpuSuggestionGpu.md) |  | 
**suggestion** | [**GpuSuggestionCheaper**](GpuSuggestionCheaper.md) | Set only when status is &#x60;suggestion&#x60;. | 

## Example

```python
from gpuai_sdk.models.gpu_suggestion import GpuSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of GpuSuggestion from a JSON string
gpu_suggestion_instance = GpuSuggestion.from_json(json)
# print the JSON string representation of the object
print(GpuSuggestion.to_json())

# convert the object into a dict
gpu_suggestion_dict = gpu_suggestion_instance.to_dict()
# create an instance of GpuSuggestion from a dict
gpu_suggestion_from_dict = GpuSuggestion.from_dict(gpu_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


