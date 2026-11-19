# DedicatedIPOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**allowed_ports** | **str** | Ports and port ranges a launch may forward, e.g. &#x60;80,443,1024-65535&#x60;. | 
**default_ports** | **List[int]** | Ports forwarded when the request names none. | 
**max_ports** | **int** | Most ports one address may forward. | 
**hourly_fee** | **float** | USD per hour while attached, from the instance becoming running until release. | 
**transfer_price_per_gb** | **float** | USD per GB through the address, inbound and outbound. | 
**transfer_included_gb** | **float** | GB of transfer per attachment that is not charged. | 
**transfer_cap_gb** | **float** | GB per attachment after which forwarding is suspended. | 
**org_limit** | **int** | Most dedicated IPs the organization may hold at once. | 
**org_in_use** | **int** | Dedicated IPs the organization holds now. | 
**available** | **int** | Addresses free for a new launch right now. | 
**acceptable_use** | **str** | The acceptable use policy for dedicated IPs. | 

## Example

```python
from gpuai_sdk.models.dedicated_ip_offer import DedicatedIPOffer

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedIPOffer from a JSON string
dedicated_ip_offer_instance = DedicatedIPOffer.from_json(json)
# print the JSON string representation of the object
print(DedicatedIPOffer.to_json())

# convert the object into a dict
dedicated_ip_offer_dict = dedicated_ip_offer_instance.to_dict()
# create an instance of DedicatedIPOffer from a dict
dedicated_ip_offer_from_dict = DedicatedIPOffer.from_dict(dedicated_ip_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


