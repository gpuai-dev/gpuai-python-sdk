# GPUStockType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** |  | [optional] 
**gpu_count** | **int** | GPUs per machine. | [optional] 
**vram_gb** | **int** | Memory per GPU. | [optional] 
**in_stock** | **bool** |  | [optional] 
**price_per_hour** | **float** | Cheapest machine in stock, USD per hour for the whole machine; 0 when not in stock. | [optional] 
**highest_price_per_hour** | **float** | Dearest machine in stock, on the same basis as price_per_hour; 0 when not in stock. A machine starts on the cheapest one left when it is placed, so it costs from price_per_hour up to this. | [optional] 
**regions** | **List[str]** | Regions with one in stock. | [optional] 
**vm_in_stock** | **bool** | In stock as a whole VM, where launches place first; price_per_hour is then the VM price. | [optional] 

## Example

```python
from gpuai_sdk.models.gpu_stock_type import GPUStockType

# TODO update the JSON string below
json = "{}"
# create an instance of GPUStockType from a JSON string
gpu_stock_type_instance = GPUStockType.from_json(json)
# print the JSON string representation of the object
print(GPUStockType.to_json())

# convert the object into a dict
gpu_stock_type_dict = gpu_stock_type_instance.to_dict()
# create an instance of GPUStockType from a dict
gpu_stock_type_from_dict = GPUStockType.from_dict(gpu_stock_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


