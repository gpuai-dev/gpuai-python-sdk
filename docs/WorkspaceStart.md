# WorkspaceStart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** | Another GPU type to start on (switch GPU). | [optional] 
**gpu_count** | **int** |  | [optional] 
**offering_id** | **str** |  | [optional] 
**max_price_per_hour** | **float** | Highest hourly GPU price, USD; null removes it. Kept for later starts; raise it to start on a pricier GPU. | [optional] 

## Example

```python
from gpuai_sdk.models.workspace_start import WorkspaceStart

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceStart from a JSON string
workspace_start_instance = WorkspaceStart.from_json(json)
# print the JSON string representation of the object
print(WorkspaceStart.to_json())

# convert the object into a dict
workspace_start_dict = workspace_start_instance.to_dict()
# create an instance of WorkspaceStart from a dict
workspace_start_from_dict = WorkspaceStart.from_dict(workspace_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


