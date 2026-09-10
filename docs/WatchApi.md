# gpuai_sdk.WatchApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_watch_rule**](WatchApi.md#create_watch_rule) | **POST** /watch-rules | Create a watch rule
[**delete_watch_rule**](WatchApi.md#delete_watch_rule) | **DELETE** /watch-rules/{id} | Delete a watch rule
[**get_watch_rule**](WatchApi.md#get_watch_rule) | **GET** /watch-rules/{id} | Get a watch rule
[**list_watch_rules**](WatchApi.md#list_watch_rules) | **GET** /watch-rules | List watch rules
[**update_watch_rule**](WatchApi.md#update_watch_rule) | **PATCH** /watch-rules/{id} | Update a watch rule


# **create_watch_rule**
> WatchRule create_watch_rule(watch_rule_create, idempotency_key=idempotency_key)

Create a watch rule

Creates a rule that notifies you when the market moves on a GPU model. Requires the `watch:write` scope (or `full_access`).

A watch rule ONLY notifies. It cannot launch capacity and cannot spend money: there is no field on this resource that provisions anything. Automatic launching is a separate resource with its own spend-consent gate.

Targeting is dimensional — a GPU model plus optional canonical region and capacity class. It is deliberately NOT possible to pin a rule to a specific catalog listing: listing identity is unstable, so a pinned rule can silently match nothing and never fire.

Delivery is to the organization's registered webhook endpoints, plus an email to the rule's creator. `webhook_endpoint_override_id` routes one rule to one specific endpoint and is the id of an endpoint already registered via `/webhook-endpoints` — the resource accepts no URL of any kind.

Organizations are limited to 50 ENABLED rules; the 422 names the limit.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.watch_rule import WatchRule
from gpuai_sdk.models.watch_rule_create import WatchRuleCreate
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
    api_instance = gpuai_sdk.WatchApi(api_client)
    watch_rule_create = gpuai_sdk.WatchRuleCreate() # WatchRuleCreate | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Create a watch rule
        api_response = api_instance.create_watch_rule(watch_rule_create, idempotency_key=idempotency_key)
        print("The response of WatchApi->create_watch_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->create_watch_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watch_rule_create** | [**WatchRuleCreate**](WatchRuleCreate.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**WatchRule**](WatchRule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Validation failed — a gpu_model that is not a GPU model we list (the detail names the closest ids when there are any), an unknown condition kind, a non-canonical region, a missing threshold on a threshold condition, an override id that is not an endpoint registered by this organization, a field naming a catalog listing or a delivery address, or the enabled-rule limit already reached.  |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_watch_rule**
> delete_watch_rule(id)

Delete a watch rule

Deletes a watch rule. Requires the `watch:write` scope (or `full_access`). Deleting an already-deleted rule returns 404.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
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
    api_instance = gpuai_sdk.WatchApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a watch rule
        api_instance.delete_watch_rule(id)
    except Exception as e:
        print("Exception when calling WatchApi->delete_watch_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_watch_rule**
> WatchRule get_watch_rule(id)

Get a watch rule

Fetches one watch rule. Requires the `watch:read` scope (or `full_access`). A rule belonging to another organization returns 404 — the same answer as an id that does not exist.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.watch_rule import WatchRule
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
    api_instance = gpuai_sdk.WatchApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a watch rule
        api_response = api_instance.get_watch_rule(id)
        print("The response of WatchApi->get_watch_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->get_watch_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**WatchRule**](WatchRule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_watch_rules**
> WatchRulePage list_watch_rules(cursor=cursor, limit=limit)

List watch rules

Lists this organization's watch rules. Requires the `watch:read` scope (or `full_access`). Rules belonging to other organizations are never returned.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.watch_rule_page import WatchRulePage
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
    api_instance = gpuai_sdk.WatchApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List watch rules
        api_response = api_instance.list_watch_rules(cursor=cursor, limit=limit)
        print("The response of WatchApi->list_watch_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->list_watch_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**WatchRulePage**](WatchRulePage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_watch_rule**
> WatchRule update_watch_rule(id, watch_rule_update)

Update a watch rule

Partially updates a watch rule. Requires the `watch:write` scope (or `full_access`).

An ABSENT key keeps the stored value; an explicit `null` on `region`, `capacity_class` or `webhook_endpoint_override_id` CLEARS it back to "any" / "organization default". The two are distinguished by which keys the body carries, so send only the keys you mean to change.

Editing a rule RE-ARMS it: the fired latch describes the condition that was replaced, so carrying it across an edit would suppress the first alert on the new one.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.watch_rule import WatchRule
from gpuai_sdk.models.watch_rule_update import WatchRuleUpdate
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
    api_instance = gpuai_sdk.WatchApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    watch_rule_update = gpuai_sdk.WatchRuleUpdate() # WatchRuleUpdate | 

    try:
        # Update a watch rule
        api_response = api_instance.update_watch_rule(id, watch_rule_update)
        print("The response of WatchApi->update_watch_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WatchApi->update_watch_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **watch_rule_update** | [**WatchRuleUpdate**](WatchRuleUpdate.md)|  | 

### Return type

[**WatchRule**](WatchRule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Validation failed against the MERGED rule — for example switching to a threshold condition on a rule that has no stored threshold, or re-targeting the rule at a gpu_model we do not list. A gpu_model already stored is only re-checked when the key is SENT, so a rule can always be parked or deleted whatever it holds.  |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

