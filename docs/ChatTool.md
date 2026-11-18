# ChatTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**function** | [**ChatToolFunction**](ChatToolFunction.md) |  | 

## Example

```python
from gpuai_sdk.models.chat_tool import ChatTool

# TODO update the JSON string below
json = "{}"
# create an instance of ChatTool from a JSON string
chat_tool_instance = ChatTool.from_json(json)
# print the JSON string representation of the object
print(ChatTool.to_json())

# convert the object into a dict
chat_tool_dict = chat_tool_instance.to_dict()
# create an instance of ChatTool from a dict
chat_tool_from_dict = ChatTool.from_dict(chat_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


