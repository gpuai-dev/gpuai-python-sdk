# WorkspaceMachine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**gpu_type** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**price_per_hour** | **float** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**ready_at** | **datetime** |  | [optional] 
**stopped_at** | **datetime** |  | [optional] 
**stop_reason** | **str** |  | [optional] 

## Example

```python
from gpuai_sdk.models.workspace_machine import WorkspaceMachine

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMachine from a JSON string
workspace_machine_instance = WorkspaceMachine.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMachine.to_json())

# convert the object into a dict
workspace_machine_dict = workspace_machine_instance.to_dict()
# create an instance of WorkspaceMachine from a dict
workspace_machine_from_dict = WorkspaceMachine.from_dict(workspace_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


