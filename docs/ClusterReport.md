# ClusterReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** |  | [optional] 
**ray_ready** | **bool** |  | [optional] 
**agent_error** | **str** |  | [optional] 
**reported_at** | **datetime** |  | [optional] 

## Example

```python
from gpuai_sdk.models.cluster_report import ClusterReport

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterReport from a JSON string
cluster_report_instance = ClusterReport.from_json(json)
# print the JSON string representation of the object
print(ClusterReport.to_json())

# convert the object into a dict
cluster_report_dict = cluster_report_instance.to_dict()
# create an instance of ClusterReport from a dict
cluster_report_from_dict = ClusterReport.from_dict(cluster_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


