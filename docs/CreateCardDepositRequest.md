# CreateCardDepositRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** | Amount in USD cents. Minimum 500 ($5.00). | 
**payment_method_id** | **str** | A saved card id from &#x60;GET /billing/payment-methods&#x60;. Omit to charge the default card (the one auto-pay uses).  | [optional] 

## Example

```python
from gpuai_sdk.models.create_card_deposit_request import CreateCardDepositRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCardDepositRequest from a JSON string
create_card_deposit_request_instance = CreateCardDepositRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCardDepositRequest.to_json())

# convert the object into a dict
create_card_deposit_request_dict = create_card_deposit_request_instance.to_dict()
# create an instance of CreateCardDepositRequest from a dict
create_card_deposit_request_from_dict = CreateCardDepositRequest.from_dict(create_card_deposit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


