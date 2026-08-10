# TemplatePortsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | [optional] 
**protocol** | **str** |  | [optional] 
**primary** | **bool** |  | [optional] 

## Example

```python
from gpuai_sdk.models.template_ports_inner import TemplatePortsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePortsInner from a JSON string
template_ports_inner_instance = TemplatePortsInner.from_json(json)
# print the JSON string representation of the object
print(TemplatePortsInner.to_json())

# convert the object into a dict
template_ports_inner_dict = template_ports_inner_instance.to_dict()
# create an instance of TemplatePortsInner from a dict
template_ports_inner_from_dict = TemplatePortsInner.from_dict(template_ports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


