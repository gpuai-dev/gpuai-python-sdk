# CardDepositStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_id** | **str** |  | 
**status** | **str** |  | 
**credited_cents** | **int** |  | [optional] 
**match** | [**CardDepositStatusMatch**](CardDepositStatusMatch.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.card_deposit_status import CardDepositStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CardDepositStatus from a JSON string
card_deposit_status_instance = CardDepositStatus.from_json(json)
# print the JSON string representation of the object
print(CardDepositStatus.to_json())

# convert the object into a dict
card_deposit_status_dict = card_deposit_status_instance.to_dict()
# create an instance of CardDepositStatus from a dict
card_deposit_status_from_dict = CardDepositStatus.from_dict(card_deposit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


