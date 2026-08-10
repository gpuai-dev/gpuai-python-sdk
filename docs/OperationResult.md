# OperationResult

Terminal-success payload. Carries the per-instance web-access credential — app_url for template deploys, terminal_url for instances provisioned with the browser web console, and the shared basic-auth login for both. The credential is also re-readable via connection.app_user/app_password on the org-scoped instance reads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_url** | **str** |  | [optional] 
**terminal_url** | **str** |  | [optional] 
**app_basic_auth_user** | **str** |  | [optional] 
**app_basic_auth_pass** | **str** |  | [optional] 

## Example

```python
from gpuai_sdk.models.operation_result import OperationResult

# TODO update the JSON string below
json = "{}"
# create an instance of OperationResult from a JSON string
operation_result_instance = OperationResult.from_json(json)
# print the JSON string representation of the object
print(OperationResult.to_json())

# convert the object into a dict
operation_result_dict = operation_result_instance.to_dict()
# create an instance of OperationResult from a dict
operation_result_from_dict = OperationResult.from_dict(operation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


