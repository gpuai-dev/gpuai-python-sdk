# Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**created** | **int** |  | [optional] 
**owned_by** | **str** |  | 
**author** | **str** | Model creator/organization (e.g. \&quot;Meta\&quot;, \&quot;Qwen\&quot;, \&quot;Black Forest Labs\&quot;). | [optional] 
**modality** | **str** |  | 
**category** | **str** | Browse-facing category; mirrors modality (chat/image/video). | [optional] 
**context_length** | **int** |  | [optional] 
**supported_parameters** | **List[str]** |  | [optional] 
**parameters** | [**List[ModelParametersInner]**](ModelParametersInner.md) | Typed parameter descriptors for media (image/video) models — name, type, enum/bounds/default. Playgrounds render input forms from these. | [optional] 
**pricing** | [**ModelPricing**](ModelPricing.md) |  | 
**aliases** | **List[str]** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from gpuai_sdk.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print(Model.to_json())

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_from_dict = Model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


