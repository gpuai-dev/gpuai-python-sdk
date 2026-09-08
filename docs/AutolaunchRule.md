# AutolaunchRule

A standing, pre-approved purchase order. It carries no upstream supplier identity, no org id, and no identifier of the API key that consented — the consenting principal is recorded in storage for the fire-time re-check, and a credential identifier has no business in a rule listing. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**gpu_model** | **str** | The GPU model the rule watches and launches, e.g. \&quot;H100\&quot;. | 
**region** | **str** | Canonical region the rule is narrowed to, or null for every region. | 
**capacity_class** | **str** | Capacity class the rule is narrowed to, or null for both. | 
**condition_kind** | **str** |  | 
**threshold** | **float** | The TRIGGER. Dollars PER GPU-HOUR for price_under, or a unit count for count_at_least. Null for in_stock. This is NOT the spend cap — see max_price_per_hour, which is in a different unit.  | 
**max_price_per_hour** | **float** | The CEILING, and the consent. Dollars per hour for the WHOLE INSTANCE, not per GPU. The launch is abandoned — never repriced — if the live price exceeds it.  | 
**max_runtime_hours** | **int** | How long an auto-launched instance may run before the platform terminates it, enforced through the instance&#39;s own auto_terminate_hours.  | 
**max_total_usd** | **float** | The worst-case total the customer approved: max_price_per_hour × max_runtime_hours, computed by the server and echoed on every read so a client never has to derive the number it is displaying.  | 
**spec** | **Dict[str, object]** | The frozen launch spec, as READ. Every value under &#x60;env&#x60; is returned as the literal &#x60;[REDACTED]&#x60; — the key names are kept so you can see what the launch will set, but the values are not readable back on any surface, by any scope. Reading a rule needs only &#x60;autolaunch:read&#x60;, which every full_access, standard and read_only key holds, so a rule listing must not be a credential listing. This changes nothing about what the rule DOES: the stored spec keeps the real values and replays them at fire time. If you need to change a token, delete the rule and create a new one.  | 
**state** | **str** | armed &#x3D; waiting for the condition. launching &#x3D; an attempt is in flight. fired &#x3D; a successful launch consumed the rule&#39;s one shot. expired &#x3D; the per-edge attempt budget ran out. A lost capacity race costs nothing and does NOT consume the shot.  | 
**attempts_this_edge** | **int** | Launch attempts made since the current condition edge began. | 
**last_failure_reason** | **str** | Why the last attempt did not buy anything: over_ceiling, capacity_race, stale_reference, key_revoked, authority_revoked or validation_failed, optionally with a colon-separated detail. Match the leading token. It never carries API key material.  | 
**launched_instance_id** | **UUID** | The instance this rule launched, once it has fired. | 
**created_by_surface** | **str** | Which entrance consented. A dashboard rule has no API key behind it, which is why its fire-time revocation failure is &#x60;authority_revoked&#x60; (the approving admin was demoted) rather than &#x60;key_revoked&#x60;.  | 
**enabled** | **bool** | False once disarmed or cancelled. A disarmed rule cannot be re-armed. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.autolaunch_rule import AutolaunchRule

# TODO update the JSON string below
json = "{}"
# create an instance of AutolaunchRule from a JSON string
autolaunch_rule_instance = AutolaunchRule.from_json(json)
# print the JSON string representation of the object
print(AutolaunchRule.to_json())

# convert the object into a dict
autolaunch_rule_dict = autolaunch_rule_instance.to_dict()
# create an instance of AutolaunchRule from a dict
autolaunch_rule_from_dict = AutolaunchRule.from_dict(autolaunch_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


