# ClusterMachine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** | The Kubernetes node name. | [optional] 
**role** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**gpu_type** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**price_per_hour** | **float** |  | [optional] 
**address** | **str** | The machine&#39;s address on the cluster network. | [optional] 
**ready_at** | **datetime** |  | [optional] 
**idle_since** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 
**terminate_reason** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_machine import ClusterMachine

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMachine from a JSON string
cluster_machine_instance = ClusterMachine.from_json(json)
# print the JSON string representation of the object
print(ClusterMachine.to_json())

# convert the object into a dict
cluster_machine_dict = cluster_machine_instance.to_dict()
# create an instance of ClusterMachine from a dict
cluster_machine_from_dict = ClusterMachine.from_dict(cluster_machine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


