# WorkspaceTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WorkspaceTemplate]**](WorkspaceTemplate.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.workspace_template_list import WorkspaceTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceTemplateList from a JSON string
workspace_template_list_instance = WorkspaceTemplateList.from_json(json)
# print the JSON string representation of the object
print(WorkspaceTemplateList.to_json())

# convert the object into a dict
workspace_template_list_dict = workspace_template_list_instance.to_dict()
# create an instance of WorkspaceTemplateList from a dict
workspace_template_list_from_dict = WorkspaceTemplateList.from_dict(workspace_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


