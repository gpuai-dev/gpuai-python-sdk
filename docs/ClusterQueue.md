# ClusterQueue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**gpu_quota** | **int** | GPUs the queue is guaranteed (-1 none). | [optional] 
**gpu_limit** | **int** | Most GPUs the queue may use (-1 no limit). | [optional] 
**allocated_gpus** | **int** |  | [optional] 
**pending_gpus** | **int** |  | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_queue import ClusterQueue

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterQueue from a JSON string
cluster_queue_instance = ClusterQueue.from_json(json)
# print the JSON string representation of the object
print(ClusterQueue.to_json())

# convert the object into a dict
cluster_queue_dict = cluster_queue_instance.to_dict()
# create an instance of ClusterQueue from a dict
cluster_queue_from_dict = ClusterQueue.from_dict(cluster_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


