# gpuai_sdk.AutolaunchApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_autolaunch_rule**](AutolaunchApi.md#create_autolaunch_rule) | **POST** /autolaunch-rules | Create an auto-launch rule (pre-approves a bounded, unattended spend)
[**delete_autolaunch_rule**](AutolaunchApi.md#delete_autolaunch_rule) | **DELETE** /autolaunch-rules/{id} | Cancel an auto-launch rule
[**disarm_autolaunch_rule**](AutolaunchApi.md#disarm_autolaunch_rule) | **PATCH** /autolaunch-rules/{id} | Disarm an auto-launch rule
[**get_autolaunch_rule**](AutolaunchApi.md#get_autolaunch_rule) | **GET** /autolaunch-rules/{id} | Get an auto-launch rule
[**list_autolaunch_rules**](AutolaunchApi.md#list_autolaunch_rules) | **GET** /autolaunch-rules | List auto-launch rules


# **create_autolaunch_rule**
> AutolaunchRule create_autolaunch_rule(autolaunch_rule_create, idempotency_key=idempotency_key)

Create an auto-launch rule (pre-approves a bounded, unattended spend)

Creates a standing, pre-approved purchase order. When the condition holds and the live price is at or under `max_price_per_hour`, the platform launches the frozen `spec` with no further confirmation from anyone — the customer is approving NOW for a purchase that happens LATER, while nobody is watching.

SCOPE. Requires the `autolaunch:write` scope, which is granted only EXPLICITLY. It is deliberately NOT covered by `full_access`, `standard` or `read_only`: `instances:write` is real-time authority, exercised with someone present, whereas this is a standing, frozen authorization that fires days later unattended. Treating them as the same authority class would have handed unattended spend authority to every key ever issued, including keys minted long before this resource existed. Most existing keys therefore receive 403 here; the correct response is to mint a key whose scopes map includes `{"autolaunch": "write"}`, never to retry, to substitute a key, or to fall back to a watch rule.

CONSENT. `acknowledged_max_total_usd` is REQUIRED and must equal `max_price_per_hour × max_runtime_hours` to within one cent. It is the API-level expression of "a valid confirmation must come AFTER the price": a caller that never computed the number cannot have shown it to anyone, and a caller that displayed a different number disagrees with what is about to be stored. Show the figure to the person approving the rule, then send it back.

TWO PRICES, TWO UNITS. `threshold` is the TRIGGER, in dollars per GPU-hour — the same unit the market chart and watch rules speak in. `max_price_per_hour` is the CEILING, in dollars per hour for the WHOLE instance. A 4-GPU rule triggering under $4.00/GPU-hr typically carries a $16.00/hr ceiling. Conflating them scales the customer's spend authorization by their GPU count.

FROZEN SPEC. `spec` is the full create-instance body the rule replays, validated at creation with the same validation a live create runs, so a spec that could never launch is refused while a human is present rather than at 3 a.m. `spec.offering_id` is REJECTED — offering identity churns between catalog polls, so a pin produces a rule that can never fire, which is the worst outcome here because the customer believes a purchase is armed. `spec.auto_terminate_hours` is overwritten from `max_runtime_hours` and must not be used to widen the bound.

Organizations are limited to 10 active rules; the 422 names the limit. The organization spending limit still applies as a backstop at fire time — a launch must fit both its own ceiling and the org cap.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.autolaunch_rule import AutolaunchRule
from gpuai_sdk.models.autolaunch_rule_create import AutolaunchRuleCreate
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
    api_instance = gpuai_sdk.AutolaunchApi(api_client)
    autolaunch_rule_create = gpuai_sdk.AutolaunchRuleCreate() # AutolaunchRuleCreate | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Create an auto-launch rule (pre-approves a bounded, unattended spend)
        api_response = api_instance.create_autolaunch_rule(autolaunch_rule_create, idempotency_key=idempotency_key)
        print("The response of AutolaunchApi->create_autolaunch_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutolaunchApi->create_autolaunch_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autolaunch_rule_create** | [**AutolaunchRuleCreate**](AutolaunchRuleCreate.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**AutolaunchRule**](AutolaunchRule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | The API key lacks &#x60;autolaunch:write&#x60;. This scope is explicit-grant only and is NOT covered by &#x60;full_access&#x60;, &#x60;standard&#x60; or &#x60;read_only&#x60;; the problem detail names the scope and the fix.  |  -  |
**422** | Validation failed — a missing or mismatched &#x60;acknowledged_max_total_usd&#x60;, a missing ceiling or runtime bound, an unknown condition kind, a non-canonical region, a missing threshold on a threshold condition, a &#x60;spec&#x60; that would not launch, a pinned &#x60;spec.offering_id&#x60;, or the active-rule limit already reached.  |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_autolaunch_rule**
> delete_autolaunch_rule(id)

Cancel an auto-launch rule

Deletes the rule and withdraws its pre-approved spend cap immediately. Requires only the `autolaunch:read` scope, for the same reason the disarm PATCH does. Deleting an already-deleted rule returns 404.


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
    api_instance = gpuai_sdk.AutolaunchApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Cancel an auto-launch rule
        api_instance.delete_autolaunch_rule(id)
    except Exception as e:
        print("Exception when calling AutolaunchApi->delete_autolaunch_rule: %s\n" % e)
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

# **disarm_autolaunch_rule**
> AutolaunchRule disarm_autolaunch_rule(id, autolaunch_rule_disarm)

Disarm an auto-launch rule

Disarms a rule. The body must be exactly `{"enabled": false}` and nothing else. Requires only the `autolaunch:read` scope — cancelling a standing spend authorization is deliberately never harder than holding one, so a key narrowed since it created a rule can still stop that rule.

This is the entire update surface, and the absence is the design. Changing a ceiling, a runtime bound, the targeting or the frozen spec is a DIFFERENT bounded purchase, so it requires deleting the rule and creating a new one through the consent gate. Re-arming is refused too: a fired rule consumed its one shot, so `{"enabled": true}` would resurrect a purchase order that was already consented to and spent.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.autolaunch_rule import AutolaunchRule
from gpuai_sdk.models.autolaunch_rule_disarm import AutolaunchRuleDisarm
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
    api_instance = gpuai_sdk.AutolaunchApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    autolaunch_rule_disarm = gpuai_sdk.AutolaunchRuleDisarm() # AutolaunchRuleDisarm | 

    try:
        # Disarm an auto-launch rule
        api_response = api_instance.disarm_autolaunch_rule(id, autolaunch_rule_disarm)
        print("The response of AutolaunchApi->disarm_autolaunch_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutolaunchApi->disarm_autolaunch_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 
 **autolaunch_rule_disarm** | [**AutolaunchRuleDisarm**](AutolaunchRuleDisarm.md)|  | 

### Return type

[**AutolaunchRule**](AutolaunchRule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | The body carried a key other than &#x60;enabled&#x60;, omitted &#x60;enabled&#x60;, or asked to re-arm the rule.  |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_autolaunch_rule**
> AutolaunchRule get_autolaunch_rule(id)

Get an auto-launch rule

Fetches one auto-launch rule, including the frozen launch spec. Requires the `autolaunch:read` scope. A rule belonging to another organization returns 404 — the same answer as an id that does not exist.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.autolaunch_rule import AutolaunchRule
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
    api_instance = gpuai_sdk.AutolaunchApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an auto-launch rule
        api_response = api_instance.get_autolaunch_rule(id)
        print("The response of AutolaunchApi->get_autolaunch_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutolaunchApi->get_autolaunch_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**|  | 

### Return type

[**AutolaunchRule**](AutolaunchRule.md)

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

# **list_autolaunch_rules**
> AutolaunchRulePage list_autolaunch_rules(cursor=cursor, limit=limit)

List auto-launch rules

Lists this organization's auto-launch rules. Requires the `autolaunch:read` scope, which `standard` and `full_access` keys carry. Rules belonging to other organizations are never returned, and rules created through the dashboard are included — the list is the organization's, not the key's.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.autolaunch_rule_page import AutolaunchRulePage
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
    api_instance = gpuai_sdk.AutolaunchApi(api_client)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List auto-launch rules
        api_response = api_instance.list_autolaunch_rules(cursor=cursor, limit=limit)
        print("The response of AutolaunchApi->list_autolaunch_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutolaunchApi->list_autolaunch_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**AutolaunchRulePage**](AutolaunchRulePage.md)

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

