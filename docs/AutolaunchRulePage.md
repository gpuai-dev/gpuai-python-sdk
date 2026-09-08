# AutolaunchRulePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AutolaunchRule]**](AutolaunchRule.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from gpuai_sdk.models.autolaunch_rule_page import AutolaunchRulePage

# TODO update the JSON string below
json = "{}"
# create an instance of AutolaunchRulePage from a JSON string
autolaunch_rule_page_instance = AutolaunchRulePage.from_json(json)
# print the JSON string representation of the object
print(AutolaunchRulePage.to_json())

# convert the object into a dict
autolaunch_rule_page_dict = autolaunch_rule_page_instance.to_dict()
# create an instance of AutolaunchRulePage from a dict
autolaunch_rule_page_from_dict = AutolaunchRulePage.from_dict(autolaunch_rule_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


