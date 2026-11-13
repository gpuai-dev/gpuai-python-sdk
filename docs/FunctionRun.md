# FunctionRun

One call of a function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**function_id** | **str** |  | 
**version_id** | **str** |  | 
**status** | **str** | queued waits for a machine; setting_up means a machine took the call and is installing the function&#39;s Python and pip requirements; running means the function body is executing. | 
**cancel_requested** | **bool** |  | 
**cold_start** | **bool** | True when the call waited for a machine to start, false when a warm machine took it. | [optional] 
**instance_id** | **str** | The machine that ran the call. It is an instance of the organization. | [optional] 
**created_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**duration_ms** | **int** | How long the function body ran. | [optional] 
**cost_usd** | **float** | The time the call held its machine, at the machine&#39;s hourly price. Machine time between calls is billed too but belongs to no call. | [optional] 
**price_per_hour** | **float** |  | [optional] 
**error** | [**FunctionRunError**](FunctionRunError.md) |  | [optional] 
**result** | **str** | The pickled return value, base64-encoded. Present only on a succeeded run fetched with include_result&#x3D;true. | [optional] 

## Example

```python
from gpuai_sdk.models.function_run import FunctionRun

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionRun from a JSON string
function_run_instance = FunctionRun.from_json(json)
# print the JSON string representation of the object
print(FunctionRun.to_json())

# convert the object into a dict
function_run_dict = function_run_instance.to_dict()
# create an instance of FunctionRun from a dict
function_run_from_dict = FunctionRun.from_dict(function_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


