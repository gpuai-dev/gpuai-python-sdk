# JobCreateRepo

A git repository cloned into `/workspace/repo`, the working directory of the command or script. Only where the deployment runs a default image. For a private repository, store a token as the organization secret `GIT_TOKEN` and name it in `secrets`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | An https URL of the repository, with no credentials in it. | 
**ref** | **str** | A branch, tag or commit. Empty means the default branch. | [optional] 

## Example

```python
from gpuai_sdk.models.job_create_repo import JobCreateRepo

# TODO update the JSON string below
json = "{}"
# create an instance of JobCreateRepo from a JSON string
job_create_repo_instance = JobCreateRepo.from_json(json)
# print the JSON string representation of the object
print(JobCreateRepo.to_json())

# convert the object into a dict
job_create_repo_dict = job_create_repo_instance.to_dict()
# create an instance of JobCreateRepo from a dict
job_create_repo_from_dict = JobCreateRepo.from_dict(job_create_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


