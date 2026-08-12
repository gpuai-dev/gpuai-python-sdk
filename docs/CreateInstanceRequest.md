# CreateInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_type** | **str** |  | 
**gpu_count** | **int** |  | 
**region** | **str** |  | [optional] 
**tier** | **str** |  | 
**ssh_key_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**max_price_per_hour** | **float** | maximum acceptable whole-instance hourly price (catalog price) | [optional] 
**template_id** | **str** | Deploy a curated application template (e.g. comfyui, vllm). When set, gpu_type may be omitted — the cheapest eligible GPU is auto-selected. For templates serving a Hugging Face model via env.MODEL (vllm, sglang), the model&#39;s published weights size is checked against the GPU&#39;s VRAM at submit time: an oversized model on an explicit gpu_type returns 422 &#x60;model_too_large&#x60; (auto-select instead raises its VRAM floor to the estimate, and 422s only when no available GPU fits). Gated/private/unknown repos are never blocked — the deploy proceeds and the 202 carries a &#x60;warnings&#x60; entry. | [optional] 
**environment** | **str** | Launch environment. Omit for the provider default (the GPU.ai Certified Image where supported). Accepted values: &#x60;certified&#x60; (the GPU.ai Certified base image), &#x60;certified:&lt;framework&gt;&#x60; (a framework layer — see GET /v1/environments for the roster, e.g. &#x60;certified:pytorch&#x60;), &#x60;certified:&lt;framework&gt;@&lt;version&gt;&#x60; (a specific framework version, e.g. &#x60;certified:pytorch@2.13&#x60;), &#x60;raw_vm&#x60; (root VM, provider default OS), &#x60;raw_vm:&lt;os&gt;&#x60; (root VM with a chosen OS, e.g. &#x60;raw_vm:ubuntu-24.04&#x60;), or &#x60;provider_template&#x60; (the provider&#39;s own image). A well-formed value the placed machine can&#39;t serve returns 422 &#x60;environment_unavailable&#x60;. | [optional] 
**offering_id** | **str** | Pin the launch to one exact offering (from GET /v1/pricing) so the engine never substitutes a pricier one. If that offering is gone, the launch fails explicitly rather than silently placing elsewhere. | [optional] 
**disk_gb** | **int** | Requested instance filesystem size in GB. Omit for the platform default (100 GB), which never narrows placement. Setting it is a hard requirement: placement narrows to capacity that can honor it (see &#x60;disk_configurable&#x60; on GET /v1/pricing), and a request no offering of the gpu_type can honor returns 422 &#x60;disk_unavailable&#x60; rather than launching with a different size. When the launch also pins an exact &#x60;offering_id&#x60;, a disk_gb larger than that offering&#39;s displayed &#x60;storage_gb&#x60; returns 422 &#x60;disk_exceeds_offering&#x60; rather than launching with a clamped filesystem. Disk beyond the included allowance (100 GB) is billed at the offering&#39;s &#x60;disk_price_per_gb_hour&#x60; (GET /v1/pricing), folded into the instance&#39;s single hourly rate. Bounds: at least 10, at most the platform ceiling (currently 1000) — outside them returns 422 &#x60;validation_failed&#x60;. | [optional] 
**env** | **Dict[str, str]** | Per-deploy env overrides; only keys the template marks user_overridable are accepted (others 422). Secret values are redacted from operation metadata. | [optional] 

## Example

```python
from gpuai_sdk.models.create_instance_request import CreateInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstanceRequest from a JSON string
create_instance_request_instance = CreateInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInstanceRequest.to_json())

# convert the object into a dict
create_instance_request_dict = create_instance_request_instance.to_dict()
# create an instance of CreateInstanceRequest from a dict
create_instance_request_from_dict = CreateInstanceRequest.from_dict(create_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


