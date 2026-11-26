# Cluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**gpu_type** | **str** |  | [optional] 
**gpus_per_node** | **int** |  | [optional] 
**min_nodes** | **int** |  | [optional] 
**max_nodes** | **int** |  | [optional] 
**regions** | **List[str]** |  | [optional] 
**placement** | **str** |  | [optional] 
**idle_timeout** | **int** |  | [optional] 
**status** | **str** | provisioning while machines start, including while the cluster is rebuilt after losing its head and while it waits for a machine to be listed (none in stock, or none at or under max_price_per_hour); ready at min_nodes ready machines; scaling while machines are added or replaced and at least one is ready to take work; failed when nothing is ready or starting because starts are refused for another reason (no balance, a spending limit, machines that do not start). The cluster keeps trying, and last_error says why. | [optional] 
**nodes** | [**ClusterNodeCounts**](ClusterNodeCounts.md) |  | [optional] 
**max_price_per_hour** | **float** |  | [optional] 
**price_per_hour** | **float** | What the cluster&#39;s machines cost now, per hour. Machines being released are not counted; a deleted cluster&#39;s price is 0. | [optional] 
**cost** | **float** | What the cluster&#39;s machines have cost so far, in USD. | [optional] 
**demand_gpus** | **int** | GPU work waiting for a machine. | [optional] 
**ray_address** | **str** |  | [optional] 
**kubernetes_url** | **str** |  | [optional] 
**last_error** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**machines** | [**List[ClusterMachine]**](ClusterMachine.md) | Returned by GET /clusters/{id} only. | [optional] 
**queues** | [**List[ClusterQueue]**](ClusterQueue.md) |  | [optional] 
**workloads** | [**List[ClusterWorkload]**](ClusterWorkload.md) |  | [optional] 
**kubernetes_nodes** | [**List[ClusterK8sNode]**](ClusterK8sNode.md) |  | [optional] 
**report** | [**ClusterReport**](ClusterReport.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print(Cluster.to_json())

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_from_dict = Cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


