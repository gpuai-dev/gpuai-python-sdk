# Operation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **UUID** |  | 
**kind** | **str** |  | 
**state** | **str** |  | 
**resource_id** | **str** |  | [optional] 
**error** | [**OperationError**](OperationError.md) |  | [optional] 
**result** | [**OperationResult**](OperationResult.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**warnings** | **List[str]** | Create-time advisories, present only on the synchronous 202 from POST /instances (never on GET /operations/{id} polls) — e.g. the model-size guard failing open because a template deploy&#39;s MODEL is a gated or unknown Hugging Face repo whose size could not be verified. | [optional] 
**hint** | **str** | Advisory pointer to Jobs (POST /jobs), present only on the synchronous 202 from POST /instances and only on some launches: when the request is a one-off batch run, or the organization launched many instances in the last 24 hours that each ran for less than 15 minutes. Same text as the GPUAI-Hint header. Never on GET /operations/{id} polls, and it never changes the launch. | [optional] 

## Example

```python
from gpuai_sdk.models.operation import Operation

# TODO update the JSON string below
json = "{}"
# create an instance of Operation from a JSON string
operation_instance = Operation.from_json(json)
# print the JSON string representation of the object
print(Operation.to_json())

# convert the object into a dict
operation_dict = operation_instance.to_dict()
# create an instance of Operation from a dict
operation_from_dict = Operation.from_dict(operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


