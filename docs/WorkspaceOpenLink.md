# WorkspaceOpenLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from gpuai_sdk.models.workspace_open_link import WorkspaceOpenLink

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceOpenLink from a JSON string
workspace_open_link_instance = WorkspaceOpenLink.from_json(json)
# print the JSON string representation of the object
print(WorkspaceOpenLink.to_json())

# convert the object into a dict
workspace_open_link_dict = workspace_open_link_instance.to_dict()
# create an instance of WorkspaceOpenLink from a dict
workspace_open_link_from_dict = WorkspaceOpenLink.from_dict(workspace_open_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


