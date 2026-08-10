# CommunityMachineDelistResult

The terminal status a machine reached after a delist. `draining` means it was occupied and the existing rental keeps running (never killed); `delisted` means it was idle and left supply immediately.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from gpuai_sdk.models.community_machine_delist_result import CommunityMachineDelistResult

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMachineDelistResult from a JSON string
community_machine_delist_result_instance = CommunityMachineDelistResult.from_json(json)
# print the JSON string representation of the object
print(CommunityMachineDelistResult.to_json())

# convert the object into a dict
community_machine_delist_result_dict = community_machine_delist_result_instance.to_dict()
# create an instance of CommunityMachineDelistResult from a dict
community_machine_delist_result_from_dict = CommunityMachineDelistResult.from_dict(community_machine_delist_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


