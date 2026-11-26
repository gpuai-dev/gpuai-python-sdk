# ClusterCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Lowercase letters, digits and hyphens, starting with a letter (32 at most). | 
**gpu_type** | **str** | GPU type of every machine; see GET /gpu-types. | 
**gpus_per_node** | **int** |  | [optional] [default to 1]
**min_nodes** | **int** | Machines kept at all times. | [optional] [default to 2]
**max_nodes** | **int** | Most machines under load. Defaults to min_nodes. | [optional] 
**regions** | **List[str]** | Canonical regions to place machines in. Empty means the cheapest suitable listing anywhere. | [optional] 
**placement** | **str** | \&quot;spread\&quot; places machines on different suppliers where it can. | [optional] [default to 'cheapest']
**idle_timeout** | **int** | Seconds a machine may run no GPU work before it is removed (down to min_nodes). | [optional] [default to 600]
**max_price_per_hour** | **float** | Highest hourly price per machine, in USD. | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_create import ClusterCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreate from a JSON string
cluster_create_instance = ClusterCreate.from_json(json)
# print the JSON string representation of the object
print(ClusterCreate.to_json())

# convert the object into a dict
cluster_create_dict = cluster_create_instance.to_dict()
# create an instance of ClusterCreate from a dict
cluster_create_from_dict = ClusterCreate.from_dict(cluster_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


