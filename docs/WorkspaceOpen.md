# WorkspaceOpen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Open a private app link to this port; omit for the IDE. | [optional] 

## Example

```python
from gpuai_sdk.models.workspace_open import WorkspaceOpen

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceOpen from a JSON string
workspace_open_instance = WorkspaceOpen.from_json(json)
# print the JSON string representation of the object
print(WorkspaceOpen.to_json())

# convert the object into a dict
workspace_open_dict = workspace_open_instance.to_dict()
# create an instance of WorkspaceOpen from a dict
workspace_open_from_dict = WorkspaceOpen.from_dict(workspace_open_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


