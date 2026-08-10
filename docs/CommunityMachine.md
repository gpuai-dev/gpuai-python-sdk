# CommunityMachine

A self-declared Community Cloud machine. Spec fields are optional and unverified until Phase 57. The enrollment token hash is never serialized.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **UUID** |  | 
**supplier_id** | **UUID** |  | 
**gpu_type** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**vram_per_gpu_gb** | **int** |  | [optional] 
**price_per_hour** | **float** |  | [optional] 
**region** | **str** |  | [optional] 
**tier** | **str** | Supplier-chosen rental model. on_demand &#x3D; guaranteed whole-node capacity; spot &#x3D; cheaper interruptible capacity. Defaults to on_demand. Becomes the catalog offering&#39;s tier. | [optional] 
**status** | **str** |  | 
**verification_status** | **str** |  | 
**last_heartbeat_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.community_machine import CommunityMachine

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityMachine from a JSON string
community_machine_instance = CommunityMachine.from_json(json)
# print the JSON string representation of the object
print(CommunityMachine.to_json())

# convert the object into a dict
community_machine_dict = community_machine_instance.to_dict()
# create an instance of CommunityMachine from a dict
community_machine_from_dict = CommunityMachine.from_dict(community_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


