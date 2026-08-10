# FineTuningJobEventList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**data** | [**List[FineTuningJobEvent]**](FineTuningJobEvent.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from gpuai_sdk.models.fine_tuning_job_event_list import FineTuningJobEventList

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuningJobEventList from a JSON string
fine_tuning_job_event_list_instance = FineTuningJobEventList.from_json(json)
# print the JSON string representation of the object
print(FineTuningJobEventList.to_json())

# convert the object into a dict
fine_tuning_job_event_list_dict = fine_tuning_job_event_list_instance.to_dict()
# create an instance of FineTuningJobEventList from a dict
fine_tuning_job_event_list_from_dict = FineTuningJobEventList.from_dict(fine_tuning_job_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


