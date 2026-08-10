# FineTuningJob

The fine-tuning job object. `status` is the COLLAPSED public enum (the rich internal states are hidden). `result_files` are freshly-presigned, short-lived download URLs regenerated per read. No backing-provider identity is present (D6).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**model** | **str** |  | 
**created_at** | **int** | Unix timestamp (seconds) at creation. | 
**finished_at** | **int** | Unix timestamp (seconds) at terminal state; null until terminal. | [optional] 
**fine_tuned_model** | **str** | Null in this release (catalog auto-serve is a later phase). | [optional] 
**status** | **str** |  | 
**training_file** | **str** |  | 
**result_files** | **List[str]** |  | 
**error** | [**FineTuningJobError**](FineTuningJobError.md) |  | [optional] 
**method** | [**FineTuningJobMethod**](FineTuningJobMethod.md) |  | [optional] 
**seed** | **int** |  | [optional] 
**suffix** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from gpuai_sdk.models.fine_tuning_job import FineTuningJob

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuningJob from a JSON string
fine_tuning_job_instance = FineTuningJob.from_json(json)
# print the JSON string representation of the object
print(FineTuningJob.to_json())

# convert the object into a dict
fine_tuning_job_dict = fine_tuning_job_instance.to_dict()
# create an instance of FineTuningJob from a dict
fine_tuning_job_from_dict = FineTuningJob.from_dict(fine_tuning_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


