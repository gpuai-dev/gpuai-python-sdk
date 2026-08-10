# Instance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**status** | **str** | Customer-facing lifecycle status. \&quot;allocating\&quot; &#x3D; the GPU is still being acquired from the provider (slow-boot capacity such as baremetal can take ~15 min); \&quot;starting\&quot; &#x3D; the node exists and is booting; \&quot;running\&quot; &#x3D; ready to use. | 
**gpu_type** | **str** |  | 
**gpu_count** | **int** |  | 
**region** | **str** |  | 
**tier** | **str** |  | 
**price_per_hour** | **float** | hourly rate for the whole instance — covers all gpu_count GPUs | 
**connection** | [**InstanceConnection**](InstanceConnection.md) |  | [optional] 
**disk_gb** | **int** | Instance filesystem size in GB that the platform configured for this launch. Present only where the placed capacity honors a configured disk size; absent means the machine&#39;s disk is provider-determined (its own flavor volume). | [optional] 
**status_reason** | **str** | Why the instance is in the error state, e.g. \&quot;provisioning stalled: the instance started but never became reachable\&quot;. Present only on errored instances. | [optional] 
**created_at** | **datetime** |  | 
**ready_at** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 

## Example

```python
from gpuai_sdk.models.instance import Instance

# TODO update the JSON string below
json = "{}"
# create an instance of Instance from a JSON string
instance_instance = Instance.from_json(json)
# print the JSON string representation of the object
print(Instance.to_json())

# convert the object into a dict
instance_dict = instance_instance.to_dict()
# create an instance of Instance from a dict
instance_from_dict = Instance.from_dict(instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


