# InstanceDedicatedIP

The instance's dedicated public IPv4 add-on. Present only on instances launched with `dedicated_ip`, and only on deployments where the add-on is enabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The GPU.ai-owned public IPv4 address. Point your DNS A record here. | 
**ports** | **List[int]** | Inbound TCP ports forwarded to the same port on the instance&#39;s loopback. | 
**status** | **str** | active means traffic is forwarded. suspended means forwarding has stopped (see suspend_reason), for example after the transfer cap was reached. released means the address was returned because the instance terminated or failed. | 
**suspend_reason** | **str** | Why forwarding is suspended, e.g. &#x60;transfer_cap&#x60;. Present only while suspended. | [optional] 
**hourly_fee** | **float** | USD per hour charged while the address is attached, locked at launch. | 
**transfer_price_per_gb** | **float** | USD per GB of traffic through the address, both directions, locked at launch. | 
**transfer_gb** | **float** | GB transferred through the address so far, both directions. | 
**charged_usd** | **float** | Total charged for this address so far (hourly fee plus transfer), in USD. | 

## Example

```python
from gpuai_sdk.models.instance_dedicated_ip import InstanceDedicatedIP

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceDedicatedIP from a JSON string
instance_dedicated_ip_instance = InstanceDedicatedIP.from_json(json)
# print the JSON string representation of the object
print(InstanceDedicatedIP.to_json())

# convert the object into a dict
instance_dedicated_ip_dict = instance_dedicated_ip_instance.to_dict()
# create an instance of InstanceDedicatedIP from a dict
instance_dedicated_ip_from_dict = InstanceDedicatedIP.from_dict(instance_dedicated_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


