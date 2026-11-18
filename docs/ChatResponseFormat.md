# ChatResponseFormat

Structured outputs. {\"type\":\"json_object\"} (JSON mode) or {\"type\":\"json_schema\",\"json_schema\":{...}}; \"text\" is the default. Only models whose /v1/models entry has supports_structured_outputs: true accept json_object / json_schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**json_schema** | [**ChatJSONSchemaFormat**](ChatJSONSchemaFormat.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.chat_response_format import ChatResponseFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ChatResponseFormat from a JSON string
chat_response_format_instance = ChatResponseFormat.from_json(json)
# print the JSON string representation of the object
print(ChatResponseFormat.to_json())

# convert the object into a dict
chat_response_format_dict = chat_response_format_instance.to_dict()
# create an instance of ChatResponseFormat from a dict
chat_response_format_from_dict = ChatResponseFormat.from_dict(chat_response_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


