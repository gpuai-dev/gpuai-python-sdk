# FineTuningJobList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**data** | [**List[FineTuningJob]**](FineTuningJob.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from gpuai_sdk.models.fine_tuning_job_list import FineTuningJobList

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuningJobList from a JSON string
fine_tuning_job_list_instance = FineTuningJobList.from_json(json)
# print the JSON string representation of the object
print(FineTuningJobList.to_json())

# convert the object into a dict
fine_tuning_job_list_dict = fine_tuning_job_list_instance.to_dict()
# create an instance of FineTuningJobList from a dict
fine_tuning_job_list_from_dict = FineTuningJobList.from_dict(fine_tuning_job_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


