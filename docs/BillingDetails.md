# BillingDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** |  | 
**address_line1** | **str** |  | 
**address_line2** | **str** |  | 
**city** | **str** |  | 
**region** | **str** |  | 
**postal_code** | **str** |  | 
**country** | **str** | ISO 3166-1 alpha-2 code, or empty. | 
**tax_id_type** | **str** | eu_vat, gb_vat, ch_vat, no_vat, us_ein, ca_bn, au_abn, nz_gst, in_gst, sg_uen, jp_cn, kr_brn, ae_trn, sa_vat, br_cnpj, mx_rfc or other. Empty when no Tax ID is stored. | 
**tax_id_masked** | **str** | The stored Tax ID, masked. Empty when none is stored. | 
**has_tax_id** | **bool** |  | 
**tax_id_enabled** | **bool** | False when this deployment cannot store a Tax ID. | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from gpuai_sdk.models.billing_details import BillingDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BillingDetails from a JSON string
billing_details_instance = BillingDetails.from_json(json)
# print the JSON string representation of the object
print(BillingDetails.to_json())

# convert the object into a dict
billing_details_dict = billing_details_instance.to_dict()
# create an instance of BillingDetails from a dict
billing_details_from_dict = BillingDetails.from_dict(billing_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


