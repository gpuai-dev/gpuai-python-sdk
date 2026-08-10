# InstanceConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**ssh_command** | **str** |  | [optional] 
**app_url** | **str** | HTTPS URL of the deployed application (template instances only), e.g. https://gpu-abcd1234.apps.gpu.ai. | [optional] 
**app_user** | **str** | HTTP Basic Auth username for app_url and terminal_url. Present on instances provisioned after the credential-persistence change; older deploys omit it (their credential was only surfaced once at deploy time). | [optional] 
**app_password** | **str** | HTTP Basic Auth password for app_url and terminal_url. Same availability as app_user. Treat as a secret. | [optional] 
**terminal_url** | **str** | HTTPS URL of the browser web console (a shell on the instance, no SSH key required), e.g. https://gpu-abcd1234-term.apps.gpu.ai. Guarded by the same app_user/app_password login. Present only on running instances provisioned with the console. | [optional] 

## Example

```python
from gpuai_sdk.models.instance_connection import InstanceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConnection from a JSON string
instance_connection_instance = InstanceConnection.from_json(json)
# print the JSON string representation of the object
print(InstanceConnection.to_json())

# convert the object into a dict
instance_connection_dict = instance_connection_instance.to_dict()
# create an instance of InstanceConnection from a dict
instance_connection_from_dict = InstanceConnection.from_dict(instance_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


