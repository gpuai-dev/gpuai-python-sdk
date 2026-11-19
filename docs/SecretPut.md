# SecretPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The secret value. Write-only; never returned. | 
**description** | **str** | Omit to keep the current description. | [optional] 

## Example

```python
from gpuai_sdk.models.secret_put import SecretPut

# TODO update the JSON string below
json = "{}"
# create an instance of SecretPut from a JSON string
secret_put_instance = SecretPut.from_json(json)
# print the JSON string representation of the object
print(SecretPut.to_json())

# convert the object into a dict
secret_put_dict = secret_put_instance.to_dict()
# create an instance of SecretPut from a dict
secret_put_from_dict = SecretPut.from_dict(secret_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


