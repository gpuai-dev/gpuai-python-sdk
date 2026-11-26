# ClusterQueueList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClusterQueue]**](ClusterQueue.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_queue_list import ClusterQueueList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterQueueList from a JSON string
cluster_queue_list_instance = ClusterQueueList.from_json(json)
# print the JSON string representation of the object
print(ClusterQueueList.to_json())

# convert the object into a dict
cluster_queue_list_dict = cluster_queue_list_instance.to_dict()
# create an instance of ClusterQueueList from a dict
cluster_queue_list_from_dict = ClusterQueueList.from_dict(cluster_queue_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


