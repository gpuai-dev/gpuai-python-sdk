# CardDeposit

A started card top-up.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_id** | **str** | Stripe PaymentIntent id (saved card) or Checkout Session id (checkout). | 
**method** | **str** |  | 
**status** | **str** | succeeded &#x3D; charged, credited by webhook within seconds. processing &#x3D; the issuer has not settled yet. requires_action &#x3D; open &#x60;action_url&#x60; to finish 3-D Secure. awaiting_payment &#x3D; open &#x60;checkout_url&#x60; to pay.  | 
**amount_cents** | **int** |  | 
**card_brand** | **str** |  | [optional] 
**card_last4** | **str** |  | [optional] 
**action_url** | **str** | Hosted 3-D Secure page (status requires_action only). | [optional] 
**checkout_url** | **str** | Stripe Checkout page (method checkout only). | [optional] 

## Example

```python
from gpuai_sdk.models.card_deposit import CardDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of CardDeposit from a JSON string
card_deposit_instance = CardDeposit.from_json(json)
# print the JSON string representation of the object
print(CardDeposit.to_json())

# convert the object into a dict
card_deposit_dict = card_deposit_instance.to_dict()
# create an instance of CardDeposit from a dict
card_deposit_from_dict = CardDeposit.from_dict(card_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


