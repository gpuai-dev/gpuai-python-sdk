# WatchRulePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WatchRule]**](WatchRule.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from gpuai_sdk.models.watch_rule_page import WatchRulePage

# TODO update the JSON string below
json = "{}"
# create an instance of WatchRulePage from a JSON string
watch_rule_page_instance = WatchRulePage.from_json(json)
# print the JSON string representation of the object
print(WatchRulePage.to_json())

# convert the object into a dict
watch_rule_page_dict = watch_rule_page_instance.to_dict()
# create an instance of WatchRulePage from a dict
watch_rule_page_from_dict = WatchRulePage.from_dict(watch_rule_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


