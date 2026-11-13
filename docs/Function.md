# Function

A Python function registered with GPU.ai. The settings are those of its current version and are null until the first version is uploaded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**status** | **str** | &#x60;running&#x60;: a call is executing. &#x60;warm&#x60;: a machine is ready and waiting. &#x60;starting&#x60;: a machine is being started. &#x60;idle&#x60;: no machine, nothing is billed. | 
**current_version_id** | **str** |  | [optional] 
**gpu** | **str** | The GPU type, or null when the cheapest GPU that fits is used. | [optional] 
**gpu_count** | **int** |  | [optional] 
**min_vram_gb** | **int** |  | [optional] 
**regions** | **List[str]** |  | [optional] 
**max_price_per_hour** | **float** |  | [optional] 
**python_version** | **str** |  | [optional] 
**pip** | **List[str]** |  | [optional] 
**timeout** | **int** | Seconds one call may run before it is stopped. | [optional] 
**idle_timeout** | **int** | Seconds a machine stays ready after a call. | [optional] 
**max_concurrency** | **int** | Most machines running calls at once. | [optional] 
**replicas** | [**FunctionReplicaCounts**](FunctionReplicaCounts.md) |  | 
**runs_queued** | **int** |  | 
**runs_24h** | **int** |  | 
**run_cost_24h_usd** | **float** | Sum of the cost of the runs created in the last 24 hours. | 
**machine_cost_24h_usd** | **float** | What the function&#39;s machines were billed in the last 24 hours, including start-up and idle time that belongs to no run. | 
**last_run_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.function import Function

# TODO update the JSON string below
json = "{}"
# create an instance of Function from a JSON string
function_instance = Function.from_json(json)
# print the JSON string representation of the object
print(Function.to_json())

# convert the object into a dict
function_dict = function_instance.to_dict()
# create an instance of Function from a dict
function_from_dict = Function.from_dict(function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


