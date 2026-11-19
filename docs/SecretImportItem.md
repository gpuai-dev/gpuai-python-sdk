# SecretImportItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from gpuai_sdk.models.secret_import_item import SecretImportItem

# TODO update the JSON string below
json = "{}"
# create an instance of SecretImportItem from a JSON string
secret_import_item_instance = SecretImportItem.from_json(json)
# print the JSON string representation of the object
print(SecretImportItem.to_json())

# convert the object into a dict
secret_import_item_dict = secret_import_item_instance.to_dict()
# create an instance of SecretImportItem from a dict
secret_import_item_from_dict = SecretImportItem.from_dict(secret_import_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


