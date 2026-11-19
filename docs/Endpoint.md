# Endpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**model** | **str** |  | 
**gpu_type** | **str** |  | 
**status** | **str** |  | 
**url** | **str** | OpenAI-compatible base URL. Set an OpenAI client&#39;s base_url to it and use a GPU.ai API key. | 
**min_replicas** | **int** |  | 
**max_replicas** | **int** |  | 
**idle_timeout** | **int** |  | 
**target_concurrency** | **int** |  | 
**max_price_per_hour** | **float** |  | 
**hf_token_secret** | **str** |  | 
**replicas** | [**EndpointReplicaCounts**](EndpointReplicaCounts.md) |  | 
**request_count** | **int** |  | 
**last_request_at** | **datetime** |  | 
**last_error** | **str** | Why the latest machine failed to start, until one becomes ready. | 
**created_at** | **datetime** |  | 
**machines** | [**List[EndpointMachine]**](EndpointMachine.md) | Recent machines, newest first. Returned by GET /v1/endpoints/{id} only. | [optional] 

## Example

```python
from gpuai_sdk.models.endpoint import Endpoint

# TODO update the JSON string below
json = "{}"
# create an instance of Endpoint from a JSON string
endpoint_instance = Endpoint.from_json(json)
# print the JSON string representation of the object
print(Endpoint.to_json())

# convert the object into a dict
endpoint_dict = endpoint_instance.to_dict()
# create an instance of Endpoint from a dict
endpoint_from_dict = Endpoint.from_dict(endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


