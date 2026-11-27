# SoftwareTrial

An organization's standing in the free trial of Functions, Ray Clusters or the Cloud IDE. The same shape as JobTrial without the Jobs-only funding fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | False when this deployment runs no trial for the product. Every other field is then zero. | 
**eligible** | **bool** | True while what the product bills this organization is credited back. | 
**reason** | **str** | Why the organization is not eligible. Omitted when eligible. | [optional] 
**cap_cents** | **int** | The most the trial credits one organization, in cents. | 
**credited_cents** | **int** | Trial credit added to the balance so far, in cents. | 
**remaining_cents** | **int** | How much more of the product&#39;s cost the trial covers, in cents. | 
**message** | **str** | The line to show the user, e.g. \&quot;Your first Ray clusters are free, up to $10.\&quot; Omitted when not eligible. | [optional] 

## Example

```python
from gpuai_sdk.models.software_trial import SoftwareTrial

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareTrial from a JSON string
software_trial_instance = SoftwareTrial.from_json(json)
# print the JSON string representation of the object
print(SoftwareTrial.to_json())

# convert the object into a dict
software_trial_dict = software_trial_instance.to_dict()
# create an instance of SoftwareTrial from a dict
software_trial_from_dict = SoftwareTrial.from_dict(software_trial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


