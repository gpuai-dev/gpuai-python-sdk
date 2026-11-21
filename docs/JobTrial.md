# JobTrial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | False when this deployment runs no trial. Every other field is then zero. | 
**eligible** | **bool** | True while this organization&#39;s jobs are credited back as they run. | 
**reason** | **str** | Why the organization is not eligible. Omitted when eligible. | [optional] 
**cap_cents** | **int** | The most the trial credits one organization, in cents. | 
**credited_cents** | **int** | Trial credit added to the balance so far, in cents. | 
**remaining_cents** | **int** | How much more job cost the trial covers, in cents. | 
**message** | **str** | The line to show the user, e.g. \&quot;Your first jobs are free, up to $10.\&quot; Omitted when not eligible. | [optional] 
**funding** | **str** | How an eligible organization&#39;s trial is paid for. &#x60;credit_back&#x60;: it pays as usual and job cost is credited back. &#x60;no_deposit&#x60;: it has no balance and may submit a trial job now. &#x60;deposit_first&#x60;: it has no balance and must add credits first. Omitted when not eligible.  | [optional] 
**max_price_per_hour** | **float** | The most a trial job&#39;s GPU may cost per hour. Only with &#x60;funding&#x60; no_deposit, and only when the deployment sets such a limit (by default it sets none). | [optional] 
**max_runtime_seconds** | **int** | The longest a trial job may run. Only with &#x60;funding&#x60; no_deposit, and only when the deployment sets such a limit (by default it sets none). | [optional] 

## Example

```python
from gpuai_sdk.models.job_trial import JobTrial

# TODO update the JSON string below
json = "{}"
# create an instance of JobTrial from a JSON string
job_trial_instance = JobTrial.from_json(json)
# print the JSON string representation of the object
print(JobTrial.to_json())

# convert the object into a dict
job_trial_dict = job_trial_instance.to_dict()
# create an instance of JobTrial from a dict
job_trial_from_dict = JobTrial.from_dict(job_trial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


