# OfferingAlternative

A live catalog row a launch whose pinned offering was gone could take instead. Same fields and meaning as the matching GET /pricing row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offering_id** | **str** |  | 
**gpu_type** | **str** |  | 
**gpu_count** | **int** |  | 
**region** | **str** |  | 
**tier** | **str** |  | 
**price_per_hour** | **float** |  | 
**available** | **int** |  | 

## Example

```python
from gpuai_sdk.models.offering_alternative import OfferingAlternative

# TODO update the JSON string below
json = "{}"
# create an instance of OfferingAlternative from a JSON string
offering_alternative_instance = OfferingAlternative.from_json(json)
# print the JSON string representation of the object
print(OfferingAlternative.to_json())

# convert the object into a dict
offering_alternative_dict = offering_alternative_instance.to_dict()
# create an instance of OfferingAlternative from a dict
offering_alternative_from_dict = OfferingAlternative.from_dict(offering_alternative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


