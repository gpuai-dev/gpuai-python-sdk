# FineTuningJobError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from gpuai_sdk.models.fine_tuning_job_error import FineTuningJobError

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuningJobError from a JSON string
fine_tuning_job_error_instance = FineTuningJobError.from_json(json)
# print the JSON string representation of the object
print(FineTuningJobError.to_json())

# convert the object into a dict
fine_tuning_job_error_dict = fine_tuning_job_error_instance.to_dict()
# create an instance of FineTuningJobError from a dict
fine_tuning_job_error_from_dict = FineTuningJobError.from_dict(fine_tuning_job_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


