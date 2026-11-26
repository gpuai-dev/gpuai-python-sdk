# ClusterK8sNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ready** | **bool** |  | [optional] 
**gpus** | **int** |  | [optional] 
**gpu_pods** | **int** |  | [optional] 
**gpus_in_use** | **int** |  | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_k8s_node import ClusterK8sNode

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterK8sNode from a JSON string
cluster_k8s_node_instance = ClusterK8sNode.from_json(json)
# print the JSON string representation of the object
print(ClusterK8sNode.to_json())

# convert the object into a dict
cluster_k8s_node_dict = cluster_k8s_node_instance.to_dict()
# create an instance of ClusterK8sNode from a dict
cluster_k8s_node_from_dict = ClusterK8sNode.from_dict(cluster_k8s_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


