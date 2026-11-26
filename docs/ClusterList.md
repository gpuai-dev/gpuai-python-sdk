# ClusterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Cluster]**](Cluster.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_list import ClusterList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterList from a JSON string
cluster_list_instance = ClusterList.from_json(json)
# print the JSON string representation of the object
print(ClusterList.to_json())

# convert the object into a dict
cluster_list_dict = cluster_list_instance.to_dict()
# create an instance of ClusterList from a dict
cluster_list_from_dict = ClusterList.from_dict(cluster_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


