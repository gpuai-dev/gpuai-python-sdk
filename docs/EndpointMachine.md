# EndpointMachine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**instance_id** | **str** | The instance the machine runs as (it appears in the instance list as ep-&lt;name&gt;-&lt;id&gt;). | 
**gpu_type** | **str** |  | 
**price_per_hour** | **float** |  | 
**ready_at** | **datetime** |  | 
**terminated_at** | **datetime** |  | 
**terminate_reason** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.endpoint_machine import EndpointMachine

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointMachine from a JSON string
endpoint_machine_instance = EndpointMachine.from_json(json)
# print the JSON string representation of the object
print(EndpointMachine.to_json())

# convert the object into a dict
endpoint_machine_dict = endpoint_machine_instance.to_dict()
# create an instance of EndpointMachine from a dict
endpoint_machine_from_dict = EndpointMachine.from_dict(endpoint_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


