# CreateFineTuningJobRequestMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**lora** | [**CreateFineTuningJobRequestMethodLora**](CreateFineTuningJobRequestMethodLora.md) |  | [optional] 

## Example

```python
from gpuai_sdk.models.create_fine_tuning_job_request_method import CreateFineTuningJobRequestMethod

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFineTuningJobRequestMethod from a JSON string
create_fine_tuning_job_request_method_instance = CreateFineTuningJobRequestMethod.from_json(json)
# print the JSON string representation of the object
print(CreateFineTuningJobRequestMethod.to_json())

# convert the object into a dict
create_fine_tuning_job_request_method_dict = create_fine_tuning_job_request_method_instance.to_dict()
# create an instance of CreateFineTuningJobRequestMethod from a dict
create_fine_tuning_job_request_method_from_dict = CreateFineTuningJobRequestMethod.from_dict(create_fine_tuning_job_request_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


