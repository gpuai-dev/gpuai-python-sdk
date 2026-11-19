# EndpointReplicaCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**starting** | **int** |  | 
**ready** | **int** |  | 

## Example

```python
from gpuai_sdk.models.endpoint_replica_counts import EndpointReplicaCounts

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointReplicaCounts from a JSON string
endpoint_replica_counts_instance = EndpointReplicaCounts.from_json(json)
# print the JSON string representation of the object
print(EndpointReplicaCounts.to_json())

# convert the object into a dict
endpoint_replica_counts_dict = endpoint_replica_counts_instance.to_dict()
# create an instance of EndpointReplicaCounts from a dict
endpoint_replica_counts_from_dict = EndpointReplicaCounts.from_dict(endpoint_replica_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


