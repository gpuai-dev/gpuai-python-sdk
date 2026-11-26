# WorkspaceUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_timeout** | **int** |  | [optional] 
**max_price_per_hour** | **float** | Highest hourly GPU price, USD; null removes it. Applies from the next start. | [optional] 

## Example

```python
from gpuai_sdk.models.workspace_update import WorkspaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUpdate from a JSON string
workspace_update_instance = WorkspaceUpdate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUpdate.to_json())

# convert the object into a dict
workspace_update_dict = workspace_update_instance.to_dict()
# create an instance of WorkspaceUpdate from a dict
workspace_update_from_dict = WorkspaceUpdate.from_dict(workspace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


