# FileObject

An uploaded file object. The storage location is an internal detail and is intentionally absent from this schema (privacy-by-omission, D6).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**bytes** | **int** |  | 
**created_at** | **int** | Unix timestamp (seconds). | 
**filename** | **str** |  | 
**purpose** | **str** |  | 

## Example

```python
from gpuai_sdk.models.file_object import FileObject

# TODO update the JSON string below
json = "{}"
# create an instance of FileObject from a JSON string
file_object_instance = FileObject.from_json(json)
# print the JSON string representation of the object
print(FileObject.to_json())

# convert the object into a dict
file_object_dict = file_object_instance.to_dict()
# create an instance of FileObject from a dict
file_object_from_dict = FileObject.from_dict(file_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


