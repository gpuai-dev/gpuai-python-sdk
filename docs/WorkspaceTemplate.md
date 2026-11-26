# WorkspaceTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**python** | **str** |  | [optional] 
**packages** | **List[str]** |  | [optional] 
**notebook** | **str** |  | [optional] 
**min_vram_gb** | **int** |  | [optional] 
**app** | [**WorkspaceTemplateApp**](WorkspaceTemplateApp.md) | The web app the template runs (ComfyUI), opened as a private app link on its port. | [optional] 

## Example

```python
from gpuai_sdk.models.workspace_template import WorkspaceTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceTemplate from a JSON string
workspace_template_instance = WorkspaceTemplate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceTemplate.to_json())

# convert the object into a dict
workspace_template_dict = workspace_template_instance.to_dict()
# create an instance of WorkspaceTemplate from a dict
workspace_template_from_dict = WorkspaceTemplate.from_dict(workspace_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


