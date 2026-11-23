# SavedCard

A saved card. Brand, last 4 digits and expiry only; never a card number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**brand** | **str** |  | 
**last4** | **str** |  | 
**exp_month** | **int** |  | 
**exp_year** | **int** |  | 
**is_default** | **bool** | The card auto-pay and an unqualified card top-up charge. | 

## Example

```python
from gpuai_sdk.models.saved_card import SavedCard

# TODO update the JSON string below
json = "{}"
# create an instance of SavedCard from a JSON string
saved_card_instance = SavedCard.from_json(json)
# print the JSON string representation of the object
print(SavedCard.to_json())

# convert the object into a dict
saved_card_dict = saved_card_instance.to_dict()
# create an instance of SavedCard from a dict
saved_card_from_dict = SavedCard.from_dict(saved_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


