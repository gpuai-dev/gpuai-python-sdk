# CreateFineTuningJobRequestMethodLora


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lora_r** | **int** |  | [optional] 
**lora_alpha** | **int** |  | [optional] 
**lora_dropout** | **float** |  | [optional] 

## Example

```python
from gpuai_sdk.models.create_fine_tuning_job_request_method_lora import CreateFineTuningJobRequestMethodLora

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFineTuningJobRequestMethodLora from a JSON string
create_fine_tuning_job_request_method_lora_instance = CreateFineTuningJobRequestMethodLora.from_json(json)
# print the JSON string representation of the object
print(CreateFineTuningJobRequestMethodLora.to_json())

# convert the object into a dict
create_fine_tuning_job_request_method_lora_dict = create_fine_tuning_job_request_method_lora_instance.to_dict()
# create an instance of CreateFineTuningJobRequestMethodLora from a dict
create_fine_tuning_job_request_method_lora_from_dict = CreateFineTuningJobRequestMethodLora.from_dict(create_fine_tuning_job_request_method_lora_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


