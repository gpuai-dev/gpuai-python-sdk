# CommunityEarnings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accrued_cents** | **int** | Lifetime accrued earnings in cents. | 
**unpaid_cents** | **int** | Accrued but not yet paid out, in cents. | 
**entries** | [**List[CommunityEarningsEntry]**](CommunityEarningsEntry.md) |  | 

## Example

```python
from gpuai_sdk.models.community_earnings import CommunityEarnings

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityEarnings from a JSON string
community_earnings_instance = CommunityEarnings.from_json(json)
# print the JSON string representation of the object
print(CommunityEarnings.to_json())

# convert the object into a dict
community_earnings_dict = community_earnings_instance.to_dict()
# create an instance of CommunityEarnings from a dict
community_earnings_from_dict = CommunityEarnings.from_dict(community_earnings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


