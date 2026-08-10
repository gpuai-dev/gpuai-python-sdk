# ModelPricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**input_per_1m_tokens_cents** | **int** |  | [optional] 
**output_per_1m_tokens_cents** | **int** |  | [optional] 
**per_image_cents** | **int** |  | [optional] 
**per_image_microcents** | **int** | Exact per-image rate in micro-cents (1e-6 cent). Prefer this for image models — per_image_cents rounds sub-cent prices to 0. | [optional] 
**per_mpxl_microcents** | **int** | Price per output megapixel in micro-cents (1e-6 cent) for image models metered per megapixel. Mutually exclusive with the per-image fields. | [optional] 
**per_video_microcents** | **int** | Representative per-clip price in micro-cents (1e-6 cent) for video models — a \&quot;from\&quot; price taken from the provider&#39;s published example rate. | [optional] 
**per_video_second_cents** | **int** |  | [optional] 
**per_video_second_microcents** | **int** | Exact per-second-of-output-video rate in micro-cents (1e-6 cent). Prefer this for video models. | [optional] 

## Example

```python
from gpuai_sdk.models.model_pricing import ModelPricing

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPricing from a JSON string
model_pricing_instance = ModelPricing.from_json(json)
# print the JSON string representation of the object
print(ModelPricing.to_json())

# convert the object into a dict
model_pricing_dict = model_pricing_instance.to_dict()
# create an instance of ModelPricing from a dict
model_pricing_from_dict = ModelPricing.from_dict(model_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


