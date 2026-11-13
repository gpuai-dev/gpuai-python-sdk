# FunctionUpload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Where to send the pickled function. | 
**method** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.function_upload import FunctionUpload

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionUpload from a JSON string
function_upload_instance = FunctionUpload.from_json(json)
# print the JSON string representation of the object
print(FunctionUpload.to_json())

# convert the object into a dict
function_upload_dict = function_upload_instance.to_dict()
# create an instance of FunctionUpload from a dict
function_upload_from_dict = FunctionUpload.from_dict(function_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


