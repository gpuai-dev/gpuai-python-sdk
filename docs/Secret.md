# Secret

An organization secret's metadata. There is no value field: values are write-only and never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The secret&#39;s name, which is also the environment variable it is delivered as. | 
**description** | **str** |  | 
**version** | **int** | How many times the value has been written. Starts at 1. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**last_used_at** | **datetime** | When the value was last delivered to a machine, or null. | 

## Example

```python
from gpuai_sdk.models.secret import Secret

# TODO update the JSON string below
json = "{}"
# create an instance of Secret from a JSON string
secret_instance = Secret.from_json(json)
# print the JSON string representation of the object
print(Secret.to_json())

# convert the object into a dict
secret_dict = secret_instance.to_dict()
# create an instance of Secret from a dict
secret_from_dict = Secret.from_dict(secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


