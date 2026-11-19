# SecretImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[SecretImportItem]**](SecretImportItem.md) |  | 
**overwrite** | **bool** | Replace the values of secrets that already exist. False leaves them untouched. | [optional] [default to False]

## Example

```python
from gpuai_sdk.models.secret_import_request import SecretImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecretImportRequest from a JSON string
secret_import_request_instance = SecretImportRequest.from_json(json)
# print the JSON string representation of the object
print(SecretImportRequest.to_json())

# convert the object into a dict
secret_import_request_dict = secret_import_request_instance.to_dict()
# create an instance of SecretImportRequest from a dict
secret_import_request_from_dict = SecretImportRequest.from_dict(secret_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


