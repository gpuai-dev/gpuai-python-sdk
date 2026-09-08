# AutolaunchRuleCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_model** | **str** |  | 
**region** | **str** | Omit or send null to consider every region. | [optional] 
**capacity_class** | **str** | Omit or send null to consider both capacity classes. | [optional] 
**condition_kind** | **str** |  | 
**threshold** | **float** | The TRIGGER, in dollars PER GPU-HOUR for price_under or a unit count for count_at_least. Required and greater than zero for both. Ignored for in_stock. Not the spend cap. Values above the maximum are refused with a 422 naming the bound — it is the largest value the column stores.  | [optional] 
**max_price_per_hour** | **float** | The CEILING, in dollars per hour for the WHOLE INSTANCE. Required even for in_stock rules: \&quot;buy it when it comes back\&quot; with no ceiling is an unbounded authorization, and this resource has no such shape. Values above the maximum are refused with a 422 naming the bound.  | 
**max_runtime_hours** | **int** |  | 
**spec** | **Dict[str, object]** | The full create-instance body this rule freezes and replays — the same shape POST /v1/instances accepts. It is modelled as an open object rather than a $ref because the instance-create body is an inline requestBody schema rather than a named component; promoting it would rewrite the instances operation and every generated client&#39;s signature for it, in a change that only needs to STORE one.  Two fields behave differently here than on a live create: &#x60;offering_id&#x60; is REJECTED (a pinned offering produces a rule that can never fire, because offering identity churns between catalog polls), and &#x60;auto_terminate_hours&#x60; is OVERWRITTEN from the rule&#39;s &#x60;max_runtime_hours&#x60; so a nested field cannot widen the runtime bound the customer approved.  | 
**acknowledged_max_total_usd** | **float** | REQUIRED. Echo of the worst-case total, max_price_per_hour × max_runtime_hours, accepted within one cent. This is the consent gate: a caller that never computed this number cannot have shown it to the person approving the rule, and a caller that displayed a different number disagrees with what is about to be stored. Either way the request is refused so the caller can re-render the real figure.  | 

## Example

```python
from gpuai_sdk.models.autolaunch_rule_create import AutolaunchRuleCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AutolaunchRuleCreate from a JSON string
autolaunch_rule_create_instance = AutolaunchRuleCreate.from_json(json)
# print the JSON string representation of the object
print(AutolaunchRuleCreate.to_json())

# convert the object into a dict
autolaunch_rule_create_dict = autolaunch_rule_create_instance.to_dict()
# create an instance of AutolaunchRuleCreate from a dict
autolaunch_rule_create_from_dict = AutolaunchRuleCreate.from_dict(autolaunch_rule_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


