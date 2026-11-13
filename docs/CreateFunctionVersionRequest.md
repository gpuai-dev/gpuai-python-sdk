# CreateFunctionVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_hash** | **str** | Lowercase hex SHA-256 over the code and everything declared about it. | 
**bundle_sha256** | **str** | Lowercase hex SHA-256 of the pickled function. | 
**bundle_bytes** | **int** | Size of the pickled function. 64 MB at most. | 
**python_version** | **str** | The Python minor version the function was pickled with, such as \&quot;3.11\&quot;. | 
**cloudpickle_version** | **str** |  | 
**pip** | **List[str]** | Requirements to install on the machine. Options (anything starting with \&quot;-\&quot;) are refused. | [optional] 
**gpu** | **str** | A GPU type from GET /gpu-types. Omit to use the cheapest GPU that fits. | [optional] 
**gpu_count** | **int** |  | [optional] [default to 1]
**min_vram_gb** | **int** | Least VRAM per GPU, used when gpu is omitted. | [optional] 
**regions** | **List[str]** |  | [optional] 
**max_price_per_hour** | **float** |  | [optional] 
**timeout** | **int** | Seconds one call may run. 1 to 86400. | 
**idle_timeout** | **int** | Seconds a machine stays ready after a call. 0 releases it at once. | [optional] [default to 300]
**max_concurrency** | **int** |  | [optional] [default to 1]

## Example

```python
from gpuai_sdk.models.create_function_version_request import CreateFunctionVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFunctionVersionRequest from a JSON string
create_function_version_request_instance = CreateFunctionVersionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFunctionVersionRequest.to_json())

# convert the object into a dict
create_function_version_request_dict = create_function_version_request_instance.to_dict()
# create an instance of CreateFunctionVersionRequest from a dict
create_function_version_request_from_dict = CreateFunctionVersionRequest.from_dict(create_function_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


