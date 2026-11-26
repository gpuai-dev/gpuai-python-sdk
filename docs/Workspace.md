# Workspace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**gpu_type** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**stop_reason** | **str** |  | [optional] 
**idle_timeout** | **int** |  | [optional] 
**max_price_per_hour** | **float** |  | [optional] 
**url** | **str** | The IDE&#39;s address; open it with a link from /workspaces/{id}/open. | [optional] 
**price_per_hour** | **float** | GPU price of the current machine (0 when stopped). | [optional] 
**storage_bytes** | **int** | Size of the last save. | [optional] 
**folder_bytes** | **int** | Size of the workspace folder now. | [optional] 
**storage_limit_bytes** | **int** |  | [optional] 
**storage_price_gb_month** | **float** |  | [optional] 
**saved_at** | **datetime** |  | [optional] 
**gpu_cost** | **float** | GPU time so far, USD. | [optional] 
**storage_cost** | **float** | Storage so far, USD. | [optional] 
**cost** | **float** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**last_active_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**machines** | [**List[WorkspaceMachine]**](WorkspaceMachine.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.workspace import Workspace

# TODO update the JSON string below
json = "{}"
# create an instance of Workspace from a JSON string
workspace_instance = Workspace.from_json(json)
# print the JSON string representation of the object
print(Workspace.to_json())

# convert the object into a dict
workspace_dict = workspace_instance.to_dict()
# create an instance of Workspace from a dict
workspace_from_dict = Workspace.from_dict(workspace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


