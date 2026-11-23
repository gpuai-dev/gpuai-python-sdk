# CreateCardCheckoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_cents** | **int** | Amount in USD cents. Minimum 500 ($5.00). | 

## Example

```python
from gpuai_sdk.models.create_card_checkout_request import CreateCardCheckoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCardCheckoutRequest from a JSON string
create_card_checkout_request_instance = CreateCardCheckoutRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCardCheckoutRequest.to_json())

# convert the object into a dict
create_card_checkout_request_dict = create_card_checkout_request_instance.to_dict()
# create an instance of CreateCardCheckoutRequest from a dict
create_card_checkout_request_from_dict = CreateCardCheckoutRequest.from_dict(create_card_checkout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


