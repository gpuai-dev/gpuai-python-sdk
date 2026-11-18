# ChatJSONSchemaFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**var_schema** | **Dict[str, object]** |  | 
**strict** | **bool** |  | [optional] 

## Example

```python
from gpuai_sdk.models.chat_json_schema_format import ChatJSONSchemaFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ChatJSONSchemaFormat from a JSON string
chat_json_schema_format_instance = ChatJSONSchemaFormat.from_json(json)
# print the JSON string representation of the object
print(ChatJSONSchemaFormat.to_json())

# convert the object into a dict
chat_json_schema_format_dict = chat_json_schema_format_instance.to_dict()
# create an instance of ChatJSONSchemaFormat from a dict
chat_json_schema_format_from_dict = ChatJSONSchemaFormat.from_dict(chat_json_schema_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


