# ListCommunityMachines200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machines** | [**List[SupplierMachineView]**](SupplierMachineView.md) |  | 

## Example

```python
from gpuai_sdk.models.list_community_machines200_response import ListCommunityMachines200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCommunityMachines200Response from a JSON string
list_community_machines200_response_instance = ListCommunityMachines200Response.from_json(json)
# print the JSON string representation of the object
print(ListCommunityMachines200Response.to_json())

# convert the object into a dict
list_community_machines200_response_dict = list_community_machines200_response_instance.to_dict()
# create an instance of ListCommunityMachines200Response from a dict
list_community_machines200_response_from_dict = ListCommunityMachines200Response.from_dict(list_community_machines200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


