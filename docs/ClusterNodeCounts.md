# ClusterNodeCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starting** | **int** |  | [optional] 
**joining** | **int** |  | [optional] 
**ready** | **int** |  | [optional] 
**draining** | **int** |  | [optional] 
**terminating** | **int** | Machines being released. A deleted cluster is &#x60;deleting&#x60; until this is 0. | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_node_counts import ClusterNodeCounts

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeCounts from a JSON string
cluster_node_counts_instance = ClusterNodeCounts.from_json(json)
# print the JSON string representation of the object
print(ClusterNodeCounts.to_json())

# convert the object into a dict
cluster_node_counts_dict = cluster_node_counts_instance.to_dict()
# create an instance of ClusterNodeCounts from a dict
cluster_node_counts_from_dict = ClusterNodeCounts.from_dict(cluster_node_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


