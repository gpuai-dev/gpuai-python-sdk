# FunctionRunLogs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FunctionRunLogChunk]**](FunctionRunLogChunk.md) |  | 
**next_cursor** | **int** | Pass as &#x60;after&#x60; on the next read. | 
**run_status** | **str** | The run&#39;s status at read time. Once it is final and data is empty, there is no more output. | 

## Example

```python
from gpuai_sdk.models.function_run_logs import FunctionRunLogs

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionRunLogs from a JSON string
function_run_logs_instance = FunctionRunLogs.from_json(json)
# print the JSON string representation of the object
print(FunctionRunLogs.to_json())

# convert the object into a dict
function_run_logs_dict = function_run_logs_instance.to_dict()
# create an instance of FunctionRunLogs from a dict
function_run_logs_from_dict = FunctionRunLogs.from_dict(function_run_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


