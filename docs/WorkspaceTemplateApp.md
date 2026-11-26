# WorkspaceTemplateApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from gpuai_sdk.models.workspace_template_app import WorkspaceTemplateApp

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceTemplateApp from a JSON string
workspace_template_app_instance = WorkspaceTemplateApp.from_json(json)
# print the JSON string representation of the object
print(WorkspaceTemplateApp.to_json())

# convert the object into a dict
workspace_template_app_dict = workspace_template_app_instance.to_dict()
# create an instance of WorkspaceTemplateApp from a dict
workspace_template_app_from_dict = WorkspaceTemplateApp.from_dict(workspace_template_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


