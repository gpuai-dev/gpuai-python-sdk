# EndpointCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Lowercase letters, digits and hyphens, starting with a letter; 48 characters at most. Unique among the organization&#39;s endpoints. | 
**model** | **str** | A Hugging Face model id. | 
**gpu_type** | **str** | The GPU each machine runs on (see GET /v1/gpu-types). At least 24 GB of memory. | 
**min_replicas** | **int** | Machines kept running even with no requests. Default 0 (scale to zero). | [optional] 
**max_replicas** | **int** | Most machines the endpoint scales out to. Default 1. | [optional] 
**idle_timeout** | **int** | Seconds without a request before a machine is released. Default 300. | [optional] 
**target_concurrency** | **int** | In-flight requests per machine before another starts. Default 16. | [optional] 
**max_price_per_hour** | **float** | Highest hourly price for a machine. | [optional] 
**hf_token_secret** | **str** | Name of an organization secret holding a Hugging Face token, delivered as HF_TOKEN (for gated models). | [optional] 

## Example

```python
from gpuai_sdk.models.endpoint_create import EndpointCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointCreate from a JSON string
endpoint_create_instance = EndpointCreate.from_json(json)
# print the JSON string representation of the object
print(EndpointCreate.to_json())

# convert the object into a dict
endpoint_create_dict = endpoint_create_instance.to_dict()
# create an instance of EndpointCreate from a dict
endpoint_create_from_dict = EndpointCreate.from_dict(endpoint_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


