# WatchRuleUpdate

Partial update. An absent key keeps the stored value; an explicit null on region, capacity_class or webhook_endpoint_override_id clears it. The merged rule is re-validated as a whole. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_model** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**capacity_class** | **str** |  | [optional] 
**condition_kind** | **str** |  | [optional] 
**threshold** | **float** |  | [optional] 
**webhook_endpoint_override_id** | **UUID** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from gpuai_sdk.models.watch_rule_update import WatchRuleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WatchRuleUpdate from a JSON string
watch_rule_update_instance = WatchRuleUpdate.from_json(json)
# print the JSON string representation of the object
print(WatchRuleUpdate.to_json())

# convert the object into a dict
watch_rule_update_dict = watch_rule_update_instance.to_dict()
# create an instance of WatchRuleUpdate from a dict
watch_rule_update_from_dict = WatchRuleUpdate.from_dict(watch_rule_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


