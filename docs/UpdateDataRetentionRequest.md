# UpdateDataRetentionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zero_data_retention** | **bool** |  | 

## Example

```python
from gpuai_sdk.models.update_data_retention_request import UpdateDataRetentionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataRetentionRequest from a JSON string
update_data_retention_request_instance = UpdateDataRetentionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDataRetentionRequest.to_json())

# convert the object into a dict
update_data_retention_request_dict = update_data_retention_request_instance.to_dict()
# create an instance of UpdateDataRetentionRequest from a dict
update_data_retention_request_from_dict = UpdateDataRetentionRequest.from_dict(update_data_retention_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


