# WatchRuleCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_model** | **str** |  | 
**region** | **str** | Omit or send null to watch every region. | [optional] 
**capacity_class** | **str** | Omit or send null to watch both capacity classes. | [optional] 
**condition_kind** | **str** |  | 
**threshold** | **float** | Required and greater than zero for price_under and count_at_least. Ignored for in_stock, which is stored with no threshold.  | [optional] 
**webhook_endpoint_override_id** | **UUID** | Id of an endpoint already registered via /webhook-endpoints. A URL here is rejected: the resource holds references, never addresses.  | [optional] 
**enabled** | **bool** | Defaults to true. Create with false to park a rule. | [optional] 

## Example

```python
from gpuai_sdk.models.watch_rule_create import WatchRuleCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WatchRuleCreate from a JSON string
watch_rule_create_instance = WatchRuleCreate.from_json(json)
# print the JSON string representation of the object
print(WatchRuleCreate.to_json())

# convert the object into a dict
watch_rule_create_dict = watch_rule_create_instance.to_dict()
# create an instance of WatchRuleCreate from a dict
watch_rule_create_from_dict = WatchRuleCreate.from_dict(watch_rule_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


