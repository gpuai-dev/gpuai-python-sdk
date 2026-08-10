# SupplierMachineView

The supplier-facing projection of a community machine. `occupied` replaces the renting customer's instance id (never exposed to the supplier); `online` is the server-derived 60s-heartbeat liveness.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **UUID** |  | 
**gpu_type** | **str** |  | [optional] 
**gpu_count** | **int** |  | [optional] 
**vram_per_gpu_gb** | **int** |  | [optional] 
**price_per_hour** | **float** | Whole-machine hourly rate (never per-GPU). | [optional] 
**region** | **str** |  | [optional] 
**tier** | **str** |  | 
**status** | **str** |  | 
**verification_status** | **str** |  | 
**online** | **bool** | Server-derived — heartbeated within the last 60 seconds. | 
**last_heartbeat_at** | **datetime** |  | [optional] 
**first_heartbeat_at** | **datetime** |  | [optional] 
**occupied** | **bool** | A customer instance is currently renting this machine. | 
**reliability_score** | **float** | Server-computed 0–100; machines below the platform threshold are auto-delisted. | [optional] 
**delist_reason** | **str** |  | [optional] 
**suspend_reason** | **str** |  | [optional] 
**agent_version** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from gpuai_sdk.models.supplier_machine_view import SupplierMachineView

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierMachineView from a JSON string
supplier_machine_view_instance = SupplierMachineView.from_json(json)
# print the JSON string representation of the object
print(SupplierMachineView.to_json())

# convert the object into a dict
supplier_machine_view_dict = supplier_machine_view_instance.to_dict()
# create an instance of SupplierMachineView from a dict
supplier_machine_view_from_dict = SupplierMachineView.from_dict(supplier_machine_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


