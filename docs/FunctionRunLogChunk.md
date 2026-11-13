# FunctionRunLogChunk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **int** |  | 
**stream** | **str** | system carries messages from the platform, such as dependency installation. | 
**data** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.function_run_log_chunk import FunctionRunLogChunk

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionRunLogChunk from a JSON string
function_run_log_chunk_instance = FunctionRunLogChunk.from_json(json)
# print the JSON string representation of the object
print(FunctionRunLogChunk.to_json())

# convert the object into a dict
function_run_log_chunk_dict = function_run_log_chunk_instance.to_dict()
# create an instance of FunctionRunLogChunk from a dict
function_run_log_chunk_from_dict = FunctionRunLogChunk.from_dict(function_run_log_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


