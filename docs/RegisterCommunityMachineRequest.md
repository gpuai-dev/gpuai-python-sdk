# RegisterCommunityMachineRequest

All fields optional; an empty body registers a zero-spec placeholder in pending_verification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**vram_per_gpu_gb** | **int** |  | [optional] 
**price_per_hour** | **float** |  | [optional] 
**region** | **str** |  | [optional] 
**tier** | **str** | Supplier-chosen rental model. Optional; omitted resolves to on_demand. spot lists the machine as cheaper interruptible capacity. | [optional] 

## Example

```python
from gpuai_sdk.models.register_community_machine_request import RegisterCommunityMachineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterCommunityMachineRequest from a JSON string
register_community_machine_request_instance = RegisterCommunityMachineRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterCommunityMachineRequest.to_json())

# convert the object into a dict
register_community_machine_request_dict = register_community_machine_request_instance.to_dict()
# create an instance of RegisterCommunityMachineRequest from a dict
register_community_machine_request_from_dict = RegisterCommunityMachineRequest.from_dict(register_community_machine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


