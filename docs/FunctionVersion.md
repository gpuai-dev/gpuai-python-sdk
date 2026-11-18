# FunctionVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**function_id** | **str** |  | 
**status** | **str** |  | 
**content_hash** | **str** |  | 
**upload** | [**FunctionUpload**](FunctionUpload.md) | Present while the bundle still has to be uploaded. | [optional] 
**python_version** | **str** |  | 
**cloudpickle_version** | **str** |  | 
**pip** | **List[str]** |  | 
**gpu** | **str** |  | [optional] 
**gpu_count** | **int** |  | 
**min_vram_gb** | **int** |  | 
**regions** | **List[str]** |  | 
**max_price_per_hour** | **float** |  | [optional] 
**timeout** | **int** |  | 
**idle_timeout** | **int** |  | 
**max_concurrency** | **int** |  | 
**secrets** | **List[str]** | Names of the organization secrets each run receives. Empty when none. | 
**created_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.function_version import FunctionVersion

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionVersion from a JSON string
function_version_instance = FunctionVersion.from_json(json)
# print the JSON string representation of the object
print(FunctionVersion.to_json())

# convert the object into a dict
function_version_dict = function_version_instance.to_dict()
# create an instance of FunctionVersion from a dict
function_version_from_dict = FunctionVersion.from_dict(function_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


