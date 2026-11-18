# OperationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Stable machine-readable failure code (see Problem.code), for example operation_failed (retryable after a backoff), price_changed or offering_unavailable (not retryable as sent). | [optional] 
**detail** | **str** |  | [optional] 
**alternatives** | [**List[OfferingAlternative]**](OfferingAlternative.md) | Present only when code is offering_unavailable: up to three live catalog rows of the same GPU type, count and tier, cheapest first. Pass one&#39;s offering_id as the new pin. | [optional] 
**current_price_per_hour** | **float** | Present only when code is price_changed: the live hourly price the launch found. | [optional] 
**max_price_per_hour** | **float** | Present only when code is price_changed: the hourly price the launch was approved at (max_price_per_hour, or the viewed price). Relaunch with max_price_per_hour of at least current_price_per_hour to accept the new price. | [optional] 

## Example

```python
from gpuai_sdk.models.operation_error import OperationError

# TODO update the JSON string below
json = "{}"
# create an instance of OperationError from a JSON string
operation_error_instance = OperationError.from_json(json)
# print the JSON string representation of the object
print(OperationError.to_json())

# convert the object into a dict
operation_error_dict = operation_error_instance.to_dict()
# create an instance of OperationError from a dict
operation_error_from_dict = OperationError.from_dict(operation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


