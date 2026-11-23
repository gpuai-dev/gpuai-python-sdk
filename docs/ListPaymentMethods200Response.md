# ListPaymentMethods200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_methods** | [**List[SavedCard]**](SavedCard.md) |  | 
**saved_card_charge_allowed** | **bool** | True when the calling key holds &#x60;payments:write&#x60;, i.e. &#x60;POST /billing/deposits/card&#x60; can succeed for it.  | 
**saved_card_charge_enabled** | **bool** | False when saved-card charging is switched off right now; use &#x60;POST /billing/deposits/card/checkout&#x60; instead.  | 
**max_charge_cents** | **int** | The per-charge limit for API card top-ups, in cents. | 
**daily_cap_cents** | **int** | The per-organization rolling-24h limit on saved-card charges, in cents. | 

## Example

```python
from gpuai_sdk.models.list_payment_methods200_response import ListPaymentMethods200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPaymentMethods200Response from a JSON string
list_payment_methods200_response_instance = ListPaymentMethods200Response.from_json(json)
# print the JSON string representation of the object
print(ListPaymentMethods200Response.to_json())

# convert the object into a dict
list_payment_methods200_response_dict = list_payment_methods200_response_instance.to_dict()
# create an instance of ListPaymentMethods200Response from a dict
list_payment_methods200_response_from_dict = ListPaymentMethods200Response.from_dict(list_payment_methods200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


