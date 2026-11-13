# CreateFunctionRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** | The version to run. Omit to run the function&#39;s current version. | [optional] 
**input** | **str** | The pickled (args, kwargs) of the call, base64-encoded. 4 MB at most before encoding. | 

## Example

```python
from gpuai_sdk.models.create_function_run_request import CreateFunctionRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFunctionRunRequest from a JSON string
create_function_run_request_instance = CreateFunctionRunRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFunctionRunRequest.to_json())

# convert the object into a dict
create_function_run_request_dict = create_function_run_request_instance.to_dict()
# create an instance of CreateFunctionRunRequest from a dict
create_function_run_request_from_dict = CreateFunctionRunRequest.from_dict(create_function_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


