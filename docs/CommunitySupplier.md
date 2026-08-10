# CommunitySupplier

One organization's Community Cloud supplier profile (ONBD-01).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier_id** | **UUID** |  | 
**org_id** | **UUID** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.community_supplier import CommunitySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CommunitySupplier from a JSON string
community_supplier_instance = CommunitySupplier.from_json(json)
# print the JSON string representation of the object
print(CommunitySupplier.to_json())

# convert the object into a dict
community_supplier_dict = community_supplier_instance.to_dict()
# create an instance of CommunitySupplier from a dict
community_supplier_from_dict = CommunitySupplier.from_dict(community_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


