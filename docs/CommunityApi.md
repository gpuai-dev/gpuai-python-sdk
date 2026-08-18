# gpuai_sdk.CommunityApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delist_community_machine**](CommunityApi.md#delist_community_machine) | **POST** /community/machines/{id}/delist | Delist a Community Cloud machine
[**enable_community_supplier**](CommunityApi.md#enable_community_supplier) | **POST** /community/suppliers | Enable the Community Cloud supplier role
[**get_community_supplier_me**](CommunityApi.md#get_community_supplier_me) | **GET** /community/suppliers/me | Get the caller&#39;s Community Cloud supplier
[**list_community_machines**](CommunityApi.md#list_community_machines) | **GET** /community/machines | List your Community Cloud machines
[**reclaim_community_machine**](CommunityApi.md#reclaim_community_machine) | **POST** /community/machines/{id}/reclaim | Reclaim a spot-tier Community Cloud machine
[**register_community_machine**](CommunityApi.md#register_community_machine) | **POST** /community/machines | Register a Community Cloud machine


# **delist_community_machine**
> CommunityMachineDelistResult delist_community_machine(id)

Delist a Community Cloud machine

Removes a machine the caller's org owns from supply (ONBD-04). Drain-not-kill: an occupied machine becomes `draining` (its customer rental keeps running until it ends naturally) and an idle machine becomes `delisted`. The endpoint never force-terminates a running rental. A missing or cross-org machine returns 404 with an indistinguishable body so existence never leaks across orgs. Requires the `community` scope (or `full_access`).

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.community_machine_delist_result import CommunityMachineDelistResult
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
    api_instance = gpuai_sdk.CommunityApi(api_client)
    id = 'id_example' # str | The machine id to delist.

    try:
        # Delist a Community Cloud machine
        api_response = api_instance.delist_community_machine(id)
        print("The response of CommunityApi->delist_community_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->delist_community_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The machine id to delist. | 

### Return type

[**CommunityMachineDelistResult**](CommunityMachineDelistResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The terminal status the machine reached. |  -  |
**403** | The community supplier role is suspended. |  -  |
**404** | The machine does not exist or is not owned by the caller&#39;s org. |  -  |
**409** | The community supplier role has not been enabled yet. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_community_supplier**
> CommunitySupplier enable_community_supplier(idempotency_key=idempotency_key)

Enable the Community Cloud supplier role

Idempotently enables the Community Cloud supplier role for the organization the API key belongs to. A repeat call is a no-op that returns the same supplier record (200, not 201). Requires the `community` scope (or `full_access`).

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.community_supplier import CommunitySupplier
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
    api_instance = gpuai_sdk.CommunityApi(api_client)
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Enable the Community Cloud supplier role
        api_response = api_instance.enable_community_supplier(idempotency_key=idempotency_key)
        print("The response of CommunityApi->enable_community_supplier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->enable_community_supplier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**CommunitySupplier**](CommunitySupplier.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The community supplier record (created or already-existing). |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community_supplier_me**
> CommunitySupplier get_community_supplier_me()

Get the caller's Community Cloud supplier

Returns the community supplier record for the organization the API key belongs to, or 404 `not-a-supplier` when the role has not been enabled. Requires the `community` scope (read).

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.community_supplier import CommunitySupplier
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
    api_instance = gpuai_sdk.CommunityApi(api_client)

    try:
        # Get the caller's Community Cloud supplier
        api_response = api_instance.get_community_supplier_me()
        print("The response of CommunityApi->get_community_supplier_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->get_community_supplier_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CommunitySupplier**](CommunitySupplier.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The community supplier record. |  -  |
**404** | The organization has not enabled the community supplier role. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_community_machines**
> ListCommunityMachines200Response list_community_machines()

List your Community Cloud machines

Returns every machine the caller's org has registered, newest first, as supplier-facing views (`occupied`/`online` projections — the renting customer's instance id is never exposed). Requires the `community` scope (read).

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.list_community_machines200_response import ListCommunityMachines200Response
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
    api_instance = gpuai_sdk.CommunityApi(api_client)

    try:
        # List your Community Cloud machines
        api_response = api_instance.list_community_machines()
        print("The response of CommunityApi->list_community_machines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->list_community_machines: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListCommunityMachines200Response**](ListCommunityMachines200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The caller&#39;s machines. |  -  |
**404** | The organization has not enabled the community supplier role. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reclaim_community_machine**
> CommunityMachineDelistResult reclaim_community_machine(id)

Reclaim a spot-tier Community Cloud machine

The spot interruption mechanic — the supplier takes back a machine they listed as interruptible (tier=spot). Drain-not-kill: an occupied machine becomes `draining` (the renter gets the grace window, surfaced to the spot router as a preemption warning) and an idle machine becomes `delisted`. An on-demand machine cannot be reclaimed (409 `machine-not-spot`) — use delist instead. Requires the `community` scope (or `full_access`).

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.community_machine_delist_result import CommunityMachineDelistResult
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
    api_instance = gpuai_sdk.CommunityApi(api_client)
    id = 'id_example' # str | The machine id to reclaim.

    try:
        # Reclaim a spot-tier Community Cloud machine
        api_response = api_instance.reclaim_community_machine(id)
        print("The response of CommunityApi->reclaim_community_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->reclaim_community_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The machine id to reclaim. | 

### Return type

[**CommunityMachineDelistResult**](CommunityMachineDelistResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status the machine reached. |  -  |
**403** | The community supplier role is suspended. |  -  |
**404** | The machine does not exist or is not owned by the caller&#39;s org. |  -  |
**409** | The supplier role has not been enabled, or the machine is on-demand capacity (&#x60;machine-not-spot&#x60;). |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_community_machine**
> CommunityMachineRegistration register_community_machine(idempotency_key=idempotency_key, register_community_machine_request=register_community_machine_request)

Register a Community Cloud machine

Registers a self-declared machine under the caller's community supplier and mints a one-time enrollment token. All spec fields are optional — an empty body registers a placeholder in `pending_verification`. The `enrollment_token` is shown exactly once and never returned again. Requires the `community` scope (or `full_access`).

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.community_machine_registration import CommunityMachineRegistration
from gpuai_sdk.models.register_community_machine_request import RegisterCommunityMachineRequest
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
    api_instance = gpuai_sdk.CommunityApi(api_client)
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    register_community_machine_request = gpuai_sdk.RegisterCommunityMachineRequest() # RegisterCommunityMachineRequest |  (optional)

    try:
        # Register a Community Cloud machine
        api_response = api_instance.register_community_machine(idempotency_key=idempotency_key, register_community_machine_request=register_community_machine_request)
        print("The response of CommunityApi->register_community_machine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunityApi->register_community_machine: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**|  | [optional] 
 **register_community_machine_request** | [**RegisterCommunityMachineRequest**](RegisterCommunityMachineRequest.md)|  | [optional] 

### Return type

[**CommunityMachineRegistration**](CommunityMachineRegistration.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The registered machine plus its one-time enrollment token. |  -  |
**403** | The community supplier role is suspended. |  -  |
**409** | The community supplier role has not been enabled yet. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

