# CommunityEarningsEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ledger_id** | **UUID** |  | 
**machine_id** | **UUID** |  | 
**instance_id** | **str** |  | 
**amount_cents** | **int** |  | 
**accrued_at** | **datetime** |  | 
**paid** | **bool** |  | 

## Example

```python
from gpuai_sdk.models.community_earnings_entry import CommunityEarningsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityEarningsEntry from a JSON string
community_earnings_entry_instance = CommunityEarningsEntry.from_json(json)
# print the JSON string representation of the object
print(CommunityEarningsEntry.to_json())

# convert the object into a dict
community_earnings_entry_dict = community_earnings_entry_instance.to_dict()
# create an instance of CommunityEarningsEntry from a dict
community_earnings_entry_from_dict = CommunityEarningsEntry.from_dict(community_earnings_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


