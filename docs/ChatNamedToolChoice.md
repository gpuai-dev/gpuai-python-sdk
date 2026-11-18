# ChatNamedToolChoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**function** | [**ChatNamedToolChoiceFunction**](ChatNamedToolChoiceFunction.md) |  | 

## Example

```python
from gpuai_sdk.models.chat_named_tool_choice import ChatNamedToolChoice

# TODO update the JSON string below
json = "{}"
# create an instance of ChatNamedToolChoice from a JSON string
chat_named_tool_choice_instance = ChatNamedToolChoice.from_json(json)
# print the JSON string representation of the object
print(ChatNamedToolChoice.to_json())

# convert the object into a dict
chat_named_tool_choice_dict = chat_named_tool_choice_instance.to_dict()
# create an instance of ChatNamedToolChoice from a dict
chat_named_tool_choice_from_dict = ChatNamedToolChoice.from_dict(chat_named_tool_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


