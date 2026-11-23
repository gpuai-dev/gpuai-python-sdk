# JobOutputFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**bytes** | **int** |  | 

## Example

```python
from gpuai_sdk.models.job_output_file import JobOutputFile

# TODO update the JSON string below
json = "{}"
# create an instance of JobOutputFile from a JSON string
job_output_file_instance = JobOutputFile.from_json(json)
# print the JSON string representation of the object
print(JobOutputFile.to_json())

# convert the object into a dict
job_output_file_dict = job_output_file_instance.to_dict()
# create an instance of JobOutputFile from a dict
job_output_file_from_dict = JobOutputFile.from_dict(job_output_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


