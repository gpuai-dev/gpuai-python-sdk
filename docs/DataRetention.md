# DataRetention


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**zero_data_retention** | **bool** | True when the org&#39;s inference requests route only to zero-data-retention model hosts. | 
**updated_at** | **datetime** | When the setting last changed; absent if it never has. | [optional] 

## Example

```python
from gpuai_sdk.models.data_retention import DataRetention

# TODO update the JSON string below
json = "{}"
# create an instance of DataRetention from a JSON string
data_retention_instance = DataRetention.from_json(json)
# print the JSON string representation of the object
print(DataRetention.to_json())

# convert the object into a dict
data_retention_dict = data_retention_instance.to_dict()
# create an instance of DataRetention from a dict
data_retention_from_dict = DataRetention.from_dict(data_retention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


