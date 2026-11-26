# GPUStockList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GPUStockType]**](GPUStockType.md) |  | [optional] 
**stock_known** | **bool** | False when the live catalog could not be read; nothing is then refused for capacity. | [optional] 

## Example

```python
from gpuai_sdk.models.gpu_stock_list import GPUStockList

# TODO update the JSON string below
json = "{}"
# create an instance of GPUStockList from a JSON string
gpu_stock_list_instance = GPUStockList.from_json(json)
# print the JSON string representation of the object
print(GPUStockList.to_json())

# convert the object into a dict
gpu_stock_list_dict = gpu_stock_list_instance.to_dict()
# create an instance of GPUStockList from a dict
gpu_stock_list_from_dict = GPUStockList.from_dict(gpu_stock_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


