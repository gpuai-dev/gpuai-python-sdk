# ClusterResize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_nodes** | **int** |  | [optional] 
**max_nodes** | **int** |  | [optional] 
**idle_timeout** | **int** |  | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_resize import ClusterResize

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterResize from a JSON string
cluster_resize_instance = ClusterResize.from_json(json)
# print the JSON string representation of the object
print(ClusterResize.to_json())

# convert the object into a dict
cluster_resize_dict = cluster_resize_instance.to_dict()
# create an instance of ClusterResize from a dict
cluster_resize_from_dict = ClusterResize.from_dict(cluster_resize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


