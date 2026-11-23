# JobInputCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The file&#39;s name. Reduced to letters, digits, dot, dash and underscore. | 
**bytes** | **int** | The file&#39;s exact size in bytes. | 

## Example

```python
from gpuai_sdk.models.job_input_create import JobInputCreate

# TODO update the JSON string below
json = "{}"
# create an instance of JobInputCreate from a JSON string
job_input_create_instance = JobInputCreate.from_json(json)
# print the JSON string representation of the object
print(JobInputCreate.to_json())

# convert the object into a dict
job_input_create_dict = job_input_create_instance.to_dict()
# create an instance of JobInputCreate from a dict
job_input_create_from_dict = JobInputCreate.from_dict(job_input_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


