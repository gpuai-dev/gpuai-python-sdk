# WorkspaceTemplateList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WorkspaceTemplate]**](WorkspaceTemplate.md) |  | [optional] 
**storage_price_gb_month** | **float** | Storage price of a saved folder, USD per GB-month (1 GB &#x3D; 1e9 bytes), charged hourly. | [optional] 
**storage_limit_bytes** | **int** | The most a workspace&#39;s saved folder may hold. | [optional] 
**save_interval_seconds** | **int** | How often a running workspace saves its folder, besides every stop. 0 means only when it stops. | [optional] 

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


