# DedicatedIPRequest

Requests a dedicated public IPv4 address for the instance. Send an empty object for the default ports (80 and 443).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | **List[int]** | Inbound TCP ports to forward. Each must be in the deployment&#39;s allowed set (see GET /dedicated-ip). Port 22 and the gateway&#39;s own ports are never allowed; SSH stays on the instance&#39;s SSH command. Omit for the defaults. | [optional] 

## Example

```python
from gpuai_sdk.models.dedicated_ip_request import DedicatedIPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedIPRequest from a JSON string
dedicated_ip_request_instance = DedicatedIPRequest.from_json(json)
# print the JSON string representation of the object
print(DedicatedIPRequest.to_json())

# convert the object into a dict
dedicated_ip_request_dict = dedicated_ip_request_instance.to_dict()
# create an instance of DedicatedIPRequest from a dict
dedicated_ip_request_from_dict = DedicatedIPRequest.from_dict(dedicated_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


