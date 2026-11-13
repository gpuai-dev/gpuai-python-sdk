# FunctionRunError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The class name of the exception the function raised, or the platform&#39;s reason: Timeout, Cancelled, LaunchError, MachineLost, DependencyError and so on. | 
**message** | **str** |  | 
**traceback** | **str** | The remote traceback, when the function raised. | [optional] 

## Example

```python
from gpuai_sdk.models.function_run_error import FunctionRunError

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionRunError from a JSON string
function_run_error_instance = FunctionRunError.from_json(json)
# print the JSON string representation of the object
print(FunctionRunError.to_json())

# convert the object into a dict
function_run_error_dict = function_run_error_instance.to_dict()
# create an instance of FunctionRunError from a dict
function_run_error_from_dict = FunctionRunError.from_dict(function_run_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


