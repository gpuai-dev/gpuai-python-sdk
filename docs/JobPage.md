# JobPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Job]**](Job.md) |  | 
**next_cursor** | **str** |  | 

## Example

```python
from gpuai_sdk.models.job_page import JobPage

# TODO update the JSON string below
json = "{}"
# create an instance of JobPage from a JSON string
job_page_instance = JobPage.from_json(json)
# print the JSON string representation of the object
print(JobPage.to_json())

# convert the object into a dict
job_page_dict = job_page_instance.to_dict()
# create an instance of JobPage from a dict
job_page_from_dict = JobPage.from_dict(job_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


