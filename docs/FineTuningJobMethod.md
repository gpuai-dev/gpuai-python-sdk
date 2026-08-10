# FineTuningJobMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**lora** | [**CreateFineTuningJobRequestMethodLora**](CreateFineTuningJobRequestMethodLora.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.fine_tuning_job_method import FineTuningJobMethod

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuningJobMethod from a JSON string
fine_tuning_job_method_instance = FineTuningJobMethod.from_json(json)
# print the JSON string representation of the object
print(FineTuningJobMethod.to_json())

# convert the object into a dict
fine_tuning_job_method_dict = fine_tuning_job_method_instance.to_dict()
# create an instance of FineTuningJobMethod from a dict
fine_tuning_job_method_from_dict = FineTuningJobMethod.from_dict(fine_tuning_job_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


