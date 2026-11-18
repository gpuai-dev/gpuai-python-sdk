# ChatMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | **str** | Message text. null on an assistant message that only calls tools. Requests may also send an array of content parts, passed through unchanged. | [optional] 
**name** | **str** |  | [optional] 
**tool_calls** | [**List[ChatToolCall]**](ChatToolCall.md) | Tool calls made by the assistant (assistant messages only). | [optional] 
**tool_call_id** | **str** | The tool call this message answers (required on role \&quot;tool\&quot;). | [optional] 

## Example

```python
from gpuai_sdk.models.chat_message import ChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessage from a JSON string
chat_message_instance = ChatMessage.from_json(json)
# print the JSON string representation of the object
print(ChatMessage.to_json())

# convert the object into a dict
chat_message_dict = chat_message_instance.to_dict()
# create an instance of ChatMessage from a dict
chat_message_from_dict = ChatMessage.from_dict(chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


