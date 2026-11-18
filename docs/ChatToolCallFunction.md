# ChatToolCallFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**arguments** | **str** | JSON-encoded arguments object, as a string. | 

## Example

```python
from gpuai_sdk.models.chat_tool_call_function import ChatToolCallFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ChatToolCallFunction from a JSON string
chat_tool_call_function_instance = ChatToolCallFunction.from_json(json)
# print the JSON string representation of the object
print(ChatToolCallFunction.to_json())

# convert the object into a dict
chat_tool_call_function_dict = chat_tool_call_function_instance.to_dict()
# create an instance of ChatToolCallFunction from a dict
chat_tool_call_function_from_dict = ChatToolCallFunction.from_dict(chat_tool_call_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


