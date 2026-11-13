# FunctionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Function]**](Function.md) |  | 

## Example

```python
from gpuai_sdk.models.function_list import FunctionList

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionList from a JSON string
function_list_instance = FunctionList.from_json(json)
# print the JSON string representation of the object
print(FunctionList.to_json())

# convert the object into a dict
function_list_dict = function_list_instance.to_dict()
# create an instance of FunctionList from a dict
function_list_from_dict = FunctionList.from_dict(function_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


