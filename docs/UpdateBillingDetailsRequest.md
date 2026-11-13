# UpdateBillingDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** | ISO 3166-1 alpha-2 code; empty clears it. | [optional] 
**tax_id_type** | **str** |  | [optional] 
**tax_id** | **str** | Write only. Stored encrypted and never returned in full. Empty removes the stored Tax ID. | [optional] 

## Example

```python
from gpuai_sdk.models.update_billing_details_request import UpdateBillingDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBillingDetailsRequest from a JSON string
update_billing_details_request_instance = UpdateBillingDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBillingDetailsRequest.to_json())

# convert the object into a dict
update_billing_details_request_dict = update_billing_details_request_instance.to_dict()
# create an instance of UpdateBillingDetailsRequest from a dict
update_billing_details_request_from_dict = UpdateBillingDetailsRequest.from_dict(update_billing_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


