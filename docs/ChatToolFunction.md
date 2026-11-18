# ChatToolFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**parameters** | **Dict[str, object]** | JSON Schema for the function arguments. | [optional] 
**strict** | **bool** |  | [optional] 

## Example

```python
from gpuai_sdk.models.chat_tool_function import ChatToolFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ChatToolFunction from a JSON string
chat_tool_function_instance = ChatToolFunction.from_json(json)
# print the JSON string representation of the object
print(ChatToolFunction.to_json())

# convert the object into a dict
chat_tool_function_dict = chat_tool_function_instance.to_dict()
# create an instance of ChatToolFunction from a dict
chat_tool_function_from_dict = ChatToolFunction.from_dict(chat_tool_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


