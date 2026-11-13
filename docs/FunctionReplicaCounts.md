# FunctionReplicaCounts

How many machines a function has in each state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starting** | **int** | Machines being started. | 
**warm** | **int** | Machines ready and waiting for a call. | 
**running** | **int** | Machines executing a call. | 

## Example

```python
from gpuai_sdk.models.function_replica_counts import FunctionReplicaCounts

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionReplicaCounts from a JSON string
function_replica_counts_instance = FunctionReplicaCounts.from_json(json)
# print the JSON string representation of the object
print(FunctionReplicaCounts.to_json())

# convert the object into a dict
function_replica_counts_dict = function_replica_counts_instance.to_dict()
# create an instance of FunctionReplicaCounts from a dict
function_replica_counts_from_dict = FunctionReplicaCounts.from_dict(function_replica_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


