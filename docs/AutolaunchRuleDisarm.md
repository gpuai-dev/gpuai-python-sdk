# AutolaunchRuleDisarm

The entire PATCH surface. `enabled` must be present and must be false. Any other key is refused rather than accepted-and-ignored, because a PATCH carrying a new ceiling that returned 200 would leave the caller believing the cap had moved. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Must be false. Sending true is refused: a fired rule consumed its one shot, so \&quot;resume\&quot; would silently be an authorization nobody gave, and arming again is a create.  | 

## Example

```python
from gpuai_sdk.models.autolaunch_rule_disarm import AutolaunchRuleDisarm

# TODO update the JSON string below
json = "{}"
# create an instance of AutolaunchRuleDisarm from a JSON string
autolaunch_rule_disarm_instance = AutolaunchRuleDisarm.from_json(json)
# print the JSON string representation of the object
print(AutolaunchRuleDisarm.to_json())

# convert the object into a dict
autolaunch_rule_disarm_dict = autolaunch_rule_disarm_instance.to_dict()
# create an instance of AutolaunchRuleDisarm from a dict
autolaunch_rule_disarm_from_dict = AutolaunchRuleDisarm.from_dict(autolaunch_rule_disarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


