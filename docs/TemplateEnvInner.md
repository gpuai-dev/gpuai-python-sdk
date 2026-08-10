# TemplateEnvInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**default** | **str** |  | [optional] 
**user_overridable** | **bool** |  | [optional] 
**secret** | **bool** |  | [optional] 

## Example

```python
from gpuai_sdk.models.template_env_inner import TemplateEnvInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEnvInner from a JSON string
template_env_inner_instance = TemplateEnvInner.from_json(json)
# print the JSON string representation of the object
print(TemplateEnvInner.to_json())

# convert the object into a dict
template_env_inner_dict = template_env_inner_instance.to_dict()
# create an instance of TemplateEnvInner from a dict
template_env_inner_from_dict = TemplateEnvInner.from_dict(template_env_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


