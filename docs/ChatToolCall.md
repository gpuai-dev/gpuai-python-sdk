# ChatToolCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**function** | [**ChatToolCallFunction**](ChatToolCallFunction.md) |  | 

## Example

```python
from gpuai_sdk.models.chat_tool_call import ChatToolCall

# TODO update the JSON string below
json = "{}"
# create an instance of ChatToolCall from a JSON string
chat_tool_call_instance = ChatToolCall.from_json(json)
# print the JSON string representation of the object
print(ChatToolCall.to_json())

# convert the object into a dict
chat_tool_call_dict = chat_tool_call_instance.to_dict()
# create an instance of ChatToolCall from a dict
chat_tool_call_from_dict = ChatToolCall.from_dict(chat_tool_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


