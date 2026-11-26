# ClusterQueueSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** |  | [optional] [default to 100]
**gpu_quota** | **int** |  | [optional] [default to -1]
**gpu_limit** | **int** |  | [optional] [default to -1]

## Example

```python
from gpuai_sdk.models.cluster_queue_set import ClusterQueueSet

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterQueueSet from a JSON string
cluster_queue_set_instance = ClusterQueueSet.from_json(json)
# print the JSON string representation of the object
print(ClusterQueueSet.to_json())

# convert the object into a dict
cluster_queue_set_dict = cluster_queue_set_instance.to_dict()
# create an instance of ClusterQueueSet from a dict
cluster_queue_set_from_dict = ClusterQueueSet.from_dict(cluster_queue_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


