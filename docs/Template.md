# Template

A deployable application template. The container image (registry path) and start command are internal orchestration details and are intentionally absent from this schema (TMPL-13 defense-by-omission).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**display_name** | **str** |  | 
**category** | **str** |  | 
**kind** | **str** | Deployable kind. \&quot;service\&quot; is a long-running app exposed at connection.app_url. \&quot;finetuning\&quot; is a run-to-completion job (no app_url) and is currently advertised only as a coming-soon catalog entry — not yet deployable. | 
**status** | **str** |  | [optional] 
**container_disk_gb** | **int** |  | [optional] 
**min_vram_gb** | **int** |  | [optional] 
**min_gpu_count** | **int** |  | [optional] 
**ports** | [**List[TemplatePortsInner]**](TemplatePortsInner.md) |  | 
**env** | [**List[TemplateEnvInner]**](TemplateEnvInner.md) |  | [optional] 
**docs_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**includes** | **List[str]** |  | [optional] 

## Example

```python
from gpuai_sdk.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


