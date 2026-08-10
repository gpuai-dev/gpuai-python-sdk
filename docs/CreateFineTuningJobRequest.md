# CreateFineTuningJobRequest

Request body for POST /fine_tuning/jobs. The `method` object carries the Axolotl LoRA/QLoRA hyperparameters; `gpuai` is a native extension for the optional budget cap and GPU preference. The backing training environment (image, GPU provider) is an internal orchestration detail and is intentionally absent from this schema (privacy-by-omission, D6).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | An operator-curated tunable base model id. | 
**training_file** | **str** | The id of a previously uploaded file (purpose&#x3D;fine-tune). | 
**suffix** | **str** |  | [optional] 
**seed** | **int** |  | [optional] 
**method** | [**CreateFineTuningJobRequestMethod**](CreateFineTuningJobRequestMethod.md) |  | 
**gpuai** | [**CreateFineTuningJobRequestGpuai**](CreateFineTuningJobRequestGpuai.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.create_fine_tuning_job_request import CreateFineTuningJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFineTuningJobRequest from a JSON string
create_fine_tuning_job_request_instance = CreateFineTuningJobRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFineTuningJobRequest.to_json())

# convert the object into a dict
create_fine_tuning_job_request_dict = create_fine_tuning_job_request_instance.to_dict()
# create an instance of CreateFineTuningJobRequest from a dict
create_fine_tuning_job_request_from_dict = CreateFineTuningJobRequest.from_dict(create_fine_tuning_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


