# ClusterWorkload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**queue** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**gpus** | **int** |  | [optional] 
**node** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_workload import ClusterWorkload

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterWorkload from a JSON string
cluster_workload_instance = ClusterWorkload.from_json(json)
# print the JSON string representation of the object
print(ClusterWorkload.to_json())

# convert the object into a dict
cluster_workload_dict = cluster_workload_instance.to_dict()
# create an instance of ClusterWorkload from a dict
cluster_workload_from_dict = ClusterWorkload.from_dict(cluster_workload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


