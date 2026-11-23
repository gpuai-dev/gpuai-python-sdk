# CardDepositStatusMatch

The deposit-match promotion's decision, once credited (absent when no promotion applied).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**match_cents** | **int** |  | 
**reason** | **str** |  | [optional] 
**hold_until** | **datetime** | Card deposits&#39; match is held until this time before it can be released. | [optional] 

## Example

```python
from gpuai_sdk.models.card_deposit_status_match import CardDepositStatusMatch

# TODO update the JSON string below
json = "{}"
# create an instance of CardDepositStatusMatch from a JSON string
card_deposit_status_match_instance = CardDepositStatusMatch.from_json(json)
# print the JSON string representation of the object
print(CardDepositStatusMatch.to_json())

# convert the object into a dict
card_deposit_status_match_dict = card_deposit_status_match_instance.to_dict()
# create an instance of CardDepositStatusMatch from a dict
card_deposit_status_match_from_dict = CardDepositStatusMatch.from_dict(card_deposit_status_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


