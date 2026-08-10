# CreateFineTuningJobRequestGpuai


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_budget_usd** | **float** |  | [optional] 
**gpu_preference** | **str** |  | [optional] 

## Example

```python
from gpuai_sdk.models.create_fine_tuning_job_request_gpuai import CreateFineTuningJobRequestGpuai

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFineTuningJobRequestGpuai from a JSON string
create_fine_tuning_job_request_gpuai_instance = CreateFineTuningJobRequestGpuai.from_json(json)
# print the JSON string representation of the object
print(CreateFineTuningJobRequestGpuai.to_json())

# convert the object into a dict
create_fine_tuning_job_request_gpuai_dict = create_fine_tuning_job_request_gpuai_instance.to_dict()
# create an instance of CreateFineTuningJobRequestGpuai from a dict
create_fine_tuning_job_request_gpuai_from_dict = CreateFineTuningJobRequestGpuai.from_dict(create_fine_tuning_job_request_gpuai_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


