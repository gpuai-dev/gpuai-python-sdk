# CommunityMachineRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine** | [**CommunityMachine**](CommunityMachine.md) |  | 
**enrollment_token** | **str** | One-time enrollment token — shown exactly once, store securely. | 

## Example

```python
from gpuai_sdk.models.community_machine_registration import CommunityMachineRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMachineRegistration from a JSON string
community_machine_registration_instance = CommunityMachineRegistration.from_json(json)
# print the JSON string representation of the object
print(CommunityMachineRegistration.to_json())

# convert the object into a dict
community_machine_registration_dict = community_machine_registration_instance.to_dict()
# create an instance of CommunityMachineRegistration from a dict
community_machine_registration_from_dict = CommunityMachineRegistration.from_dict(community_machine_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


