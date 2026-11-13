# FunctionRunList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FunctionRun]**](FunctionRun.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from gpuai_sdk.models.function_run_list import FunctionRunList

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionRunList from a JSON string
function_run_list_instance = FunctionRunList.from_json(json)
# print the JSON string representation of the object
print(FunctionRunList.to_json())

# convert the object into a dict
function_run_list_dict = function_run_list_instance.to_dict()
# create an instance of FunctionRunList from a dict
function_run_list_from_dict = FunctionRunList.from_dict(function_run_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


