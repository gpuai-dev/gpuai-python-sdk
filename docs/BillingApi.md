# gpuai_sdk.BillingApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_spending_limit**](BillingApi.md#get_spending_limit) | **GET** /billing/spending-limit | Get the org spending limit
[**update_spending_limit**](BillingApi.md#update_spending_limit) | **PUT** /billing/spending-limit | Set the org spending limit


# **get_spending_limit**
> SpendingLimit get_spending_limit()

Get the org spending limit

Returns the organization's monthly spending limit and opt-in daily spend cap, with the current month and day spend. Requires the `billing:read` scope. Returns 404 when no limit is configured.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.spending_limit import SpendingLimit
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)

    try:
        # Get the org spending limit
        api_response = api_instance.get_spending_limit()
        print("The response of BillingApi->get_spending_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_spending_limit: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SpendingLimit**](SpendingLimit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_spending_limit**
> SpendingLimit update_spending_limit(update_spending_limit_request)

Set the org spending limit

Sets the monthly spending limit and optionally sets or clears the opt-in daily spend cap. Requires the `billing:write` scope AND org-admin privileges (a non-admin member gets 403). `daily_limit_dollars` uses pointer semantics: omit to leave the cap unchanged, 0 to clear it, a positive value to set it.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.spending_limit import SpendingLimit
from gpuai_sdk.models.update_spending_limit_request import UpdateSpendingLimitRequest
from gpuai_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gpu.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gpuai_sdk.Configuration(
    host = "https://api.gpu.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (gpuai_live_<24-base62>): bearerAuth
configuration = gpuai_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gpuai_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gpuai_sdk.BillingApi(api_client)
    update_spending_limit_request = gpuai_sdk.UpdateSpendingLimitRequest() # UpdateSpendingLimitRequest | 

    try:
        # Set the org spending limit
        api_response = api_instance.update_spending_limit(update_spending_limit_request)
        print("The response of BillingApi->update_spending_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->update_spending_limit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_spending_limit_request** | [**UpdateSpendingLimitRequest**](UpdateSpendingLimitRequest.md)|  | 

### Return type

[**SpendingLimit**](SpendingLimit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Error response (RFC 7807) |  -  |
**422** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

