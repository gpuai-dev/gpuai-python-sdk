# WatchRule

A rule that notifies when the market moves on a GPU model. It carries no upstream supplier identity of any kind, and no delivery address — those are properties of the resource, not of a particular response. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**gpu_model** | **str** | The canonical GPU model id the rule watches, e.g. \&quot;h100_sxm\&quot; — a MODEL, not a generation. Alerts match the live catalog exactly, so a rule for a model we do not list could never fire and is refused rather than stored. Case and punctuation are forgiving (\&quot;H100-SXM\&quot; resolves to \&quot;h100_sxm\&quot;), and the canonical id is what is stored and returned. GET /v1/gpu-types lists the models currently on offer; a model with no stock right now is still watchable, which is the point of watching it.  | 
**region** | **str** | Canonical region the rule is narrowed to, or null for every region. | 
**capacity_class** | **str** | Capacity class the rule is narrowed to, or null for both. | 
**condition_kind** | **str** |  | 
**threshold** | **float** | Per-GPU hourly price for price_under, or a unit count for count_at_least. Null for in_stock, which takes no threshold.  | 
**state** | **str** | armed &#x3D; the condition is currently false and the next transition to true will alert. fired &#x3D; it has alerted and has not yet re-armed.  | 
**last_fired_at** | **datetime** |  | 
**quiet_until** | **datetime** | While set, the rule will not re-fire even if the condition re-crosses — the quiet window that stops a boundary-hugging signal alerting on every crossing.  | 
**webhook_endpoint_override_id** | **UUID** | Id of a webhook endpoint registered by this organization, or null to deliver to every registered endpoint. Never a URL.  | 
**enabled** | **bool** |  | 
**deactivated_reason** | **str** | Why an automatically disabled rule was disabled — for example its creator no longer belongs to the organization.  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.watch_rule import WatchRule

# TODO update the JSON string below
json = "{}"
# create an instance of WatchRule from a JSON string
watch_rule_instance = WatchRule.from_json(json)
# print the JSON string representation of the object
print(WatchRule.to_json())

# convert the object into a dict
watch_rule_dict = watch_rule_instance.to_dict()
# create an instance of WatchRule from a dict
watch_rule_from_dict = WatchRule.from_dict(watch_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


