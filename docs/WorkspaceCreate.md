# WorkspaceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Lowercase letters, digits and hyphens, starting with a letter (32 at most). | 
**template** | **str** | See GET /workspace-templates. | [optional] [default to 'pytorch']
**gpu_type** | **str** |  | 
**gpu_count** | **int** |  | [optional] [default to 1]
**idle_timeout** | **int** | Seconds without use before the workspace saves and stops. | [optional] [default to 1800]
**max_price_per_hour** | **float** |  | [optional] 
**offering_id** | **str** | Place the machine on this offering, as on instance create. | [optional] 

## Example

```python
from gpuai_sdk.models.workspace_create import WorkspaceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCreate from a JSON string
workspace_create_instance = WorkspaceCreate.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCreate.to_json())

# convert the object into a dict
workspace_create_dict = workspace_create_instance.to_dict()
# create an instance of WorkspaceCreate from a dict
workspace_create_from_dict = WorkspaceCreate.from_dict(workspace_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


