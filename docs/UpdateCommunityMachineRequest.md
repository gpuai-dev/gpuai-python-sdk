# UpdateCommunityMachineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_per_hour** | **float** | Whole-machine hourly rate (never per-GPU). Must clear the platform floor; a below-floor price is rejected with &#x60;price-below-floor&#x60; carrying the concrete &#x60;floor_per_hour&#x60;. | 

## Example

```python
from gpuai_sdk.models.update_community_machine_request import UpdateCommunityMachineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCommunityMachineRequest from a JSON string
update_community_machine_request_instance = UpdateCommunityMachineRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCommunityMachineRequest.to_json())

# convert the object into a dict
update_community_machine_request_dict = update_community_machine_request_instance.to_dict()
# create an instance of UpdateCommunityMachineRequest from a dict
update_community_machine_request_from_dict = UpdateCommunityMachineRequest.from_dict(update_community_machine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


