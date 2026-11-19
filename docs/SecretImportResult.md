# SecretImportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **List[str]** |  | 
**updated** | **List[str]** |  | 
**skipped** | **List[str]** | Names that already existed and were left untouched (overwrite false). | 

## Example

```python
from gpuai_sdk.models.secret_import_result import SecretImportResult

# TODO update the JSON string below
json = "{}"
# create an instance of SecretImportResult from a JSON string
secret_import_result_instance = SecretImportResult.from_json(json)
# print the JSON string representation of the object
print(SecretImportResult.to_json())

# convert the object into a dict
secret_import_result_dict = secret_import_result_instance.to_dict()
# create an instance of SecretImportResult from a dict
secret_import_result_from_dict = SecretImportResult.from_dict(secret_import_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


