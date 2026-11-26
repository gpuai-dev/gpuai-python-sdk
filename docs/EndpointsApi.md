# gpuai_sdk.EndpointsApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_endpoint**](EndpointsApi.md#create_endpoint) | **POST** /endpoints | Create a model endpoint
[**create_endpoint_chat_completion**](EndpointsApi.md#create_endpoint_chat_completion) | **POST** /endpoints/{id}/openai/v1/chat/completions | Chat completion on a model endpoint (OpenAI-compatible)
[**create_endpoint_completion**](EndpointsApi.md#create_endpoint_completion) | **POST** /endpoints/{id}/openai/v1/completions | Text completion on a model endpoint (OpenAI-compatible)
[**delete_endpoint**](EndpointsApi.md#delete_endpoint) | **DELETE** /endpoints/{id} | Delete a model endpoint
[**get_endpoint**](EndpointsApi.md#get_endpoint) | **GET** /endpoints/{id} | Get a model endpoint
[**list_endpoint_models**](EndpointsApi.md#list_endpoint_models) | **GET** /endpoints/{id}/openai/v1/models | List the model an endpoint serves (OpenAI-compatible)
[**list_endpoints**](EndpointsApi.md#list_endpoints) | **GET** /endpoints | List model endpoints


# **create_endpoint**
> Endpoint create_endpoint(endpoint_create)

Create a model endpoint

Creates an OpenAI-compatible endpoint serving a Hugging Face model with vLLM on the chosen GPU type. Nothing starts until the first request arrives, unless `min_replicas` keeps machines warm. Each machine is billed for the time it exists, like an instance, through the same balance. For a gated model, store a Hugging Face token as a secret and name it in `hf_token_secret`; it reaches the machines as HF_TOKEN. Returns 422 `validation_failed` for a bad field, 409 `name_taken` for a duplicate name, and 409 `limit_reached` at the per-organization cap. Requires the `functions:write` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.endpoint import Endpoint
from gpuai_sdk.models.endpoint_create import EndpointCreate
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
    api_instance = gpuai_sdk.EndpointsApi(api_client)
    endpoint_create = gpuai_sdk.EndpointCreate() # EndpointCreate | 

    try:
        # Create a model endpoint
        api_response = api_instance.create_endpoint(endpoint_create)
        print("The response of EndpointsApi->create_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->create_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_create** | [**EndpointCreate**](EndpointCreate.md)|  | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | &#x60;region_not_supported&#x60; — GPU.ai can&#39;t provide this service in the caller&#39;s country or region. Returned only for new spending (launches, deposits, key minting); reading, stopping and deleting resources are never refused, and support stays reachable.  |  -  |
**201** | Created. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_endpoint_chat_completion**
> ChatCompletionResponse create_endpoint_chat_completion(id, chat_completion_request)

Chat completion on a model endpoint (OpenAI-compatible)

The OpenAI chat completions route of one endpoint: point an OpenAI client's base_url at the endpoint's `url` and use a GPU.ai API key with the `functions:write` scope. The request's `model` is replaced with the endpoint's model, so any value works. Set `"stream": true` for Server-Sent Events, passed through as vLLM produces them. When no machine is ready the request waits while one starts (a cold start takes minutes: machine, image and model download); if none is ready in time the answer is 503 `endpoint_starting` with Retry-After. 402 `insufficient_quota` when the balance is empty. Errors use the OpenAI error envelope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.chat_completion_request import ChatCompletionRequest
from gpuai_sdk.models.chat_completion_response import ChatCompletionResponse
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
    api_instance = gpuai_sdk.EndpointsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The endpoint's id.
    chat_completion_request = gpuai_sdk.ChatCompletionRequest() # ChatCompletionRequest | 

    try:
        # Chat completion on a model endpoint (OpenAI-compatible)
        api_response = api_instance.create_endpoint_chat_completion(id, chat_completion_request)
        print("The response of EndpointsApi->create_endpoint_chat_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->create_endpoint_chat_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The endpoint&#39;s id. | 
 **chat_completion_request** | [**ChatCompletionRequest**](ChatCompletionRequest.md)|  | 

### Return type

[**ChatCompletionResponse**](ChatCompletionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json for non-streaming requests; text/event-stream when stream&#x3D;true.  |  -  |
**400** | Invalid request (OpenAI error envelope). On inference routes this includes &#x60;zero_data_retention_unavailable&#x60; when zero data retention is required and the model has no zero-data-retention host. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**402** | Insufficient balance (OpenAI error envelope, SERV-06). |  -  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or, for &#x60;POST /fine_tuning/jobs&#x60;, GPU.ai can&#39;t provide this service in the caller&#39;s country or region (&#x60;region_not_supported&#x60;). OpenAI error envelope.  |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**502** | Internal server error (OpenAI error envelope). |  -  |
**503** | Upstream provider unavailable (OpenAI error envelope). Retry-After header may indicate seconds to wait. Code &#x60;data_retention_check_failed&#x60; means the org zero data retention setting could not be read, so the request was not sent; retry shortly. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_endpoint_completion**
> Dict[str, object] create_endpoint_completion(id, request_body)

Text completion on a model endpoint (OpenAI-compatible)

The OpenAI completions route of one endpoint, with the same auth, model rewrite, streaming, cold start and error behavior as chat completions.

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
    api_instance = gpuai_sdk.EndpointsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The endpoint's id.
    request_body = None # Dict[str, Optional[object]] | 

    try:
        # Text completion on a model endpoint (OpenAI-compatible)
        api_response = api_instance.create_endpoint_completion(id, request_body)
        print("The response of EndpointsApi->create_endpoint_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->create_endpoint_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The endpoint&#39;s id. | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json for non-streaming requests; text/event-stream when stream&#x3D;true.  |  -  |
**400** | Invalid request (OpenAI error envelope). On inference routes this includes &#x60;zero_data_retention_unavailable&#x60; when zero data retention is required and the model has no zero-data-retention host. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**402** | Insufficient balance (OpenAI error envelope, SERV-06). |  -  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or, for &#x60;POST /fine_tuning/jobs&#x60;, GPU.ai can&#39;t provide this service in the caller&#39;s country or region (&#x60;region_not_supported&#x60;). OpenAI error envelope.  |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**502** | Internal server error (OpenAI error envelope). |  -  |
**503** | Upstream provider unavailable (OpenAI error envelope). Retry-After header may indicate seconds to wait. Code &#x60;data_retention_check_failed&#x60; means the org zero data retention setting could not be read, so the request was not sent; retry shortly. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint**
> delete_endpoint(id)

Delete a model endpoint

Deletes the endpoint. Its machines are released within seconds and stop billing when terminated. Requires the `functions:write` scope.

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
    api_instance = gpuai_sdk.EndpointsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The endpoint's id.

    try:
        # Delete a model endpoint
        api_instance.delete_endpoint(id)
    except Exception as e:
        print("Exception when calling EndpointsApi->delete_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The endpoint&#39;s id. | 

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
**204** | Deleted. |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint**
> Endpoint get_endpoint(id)

Get a model endpoint

Returns one endpoint with its recent machines (newest first), each with its price, ready and terminated times, and why it was released. Requires the `functions:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.endpoint import Endpoint
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
    api_instance = gpuai_sdk.EndpointsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The endpoint's id.

    try:
        # Get a model endpoint
        api_response = api_instance.get_endpoint(id)
        print("The response of EndpointsApi->get_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->get_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The endpoint&#39;s id. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The endpoint. |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_endpoint_models**
> Dict[str, object] list_endpoint_models(id)

List the model an endpoint serves (OpenAI-compatible)

The OpenAI models route of one endpoint: the one model it serves. Can trigger a cold start like any other request.

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
    api_instance = gpuai_sdk.EndpointsApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The endpoint's id.

    try:
        # List the model an endpoint serves (OpenAI-compatible)
        api_response = api_instance.list_endpoint_models(id)
        print("The response of EndpointsApi->list_endpoint_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->list_endpoint_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The endpoint&#39;s id. | 

### Return type

**Dict[str, object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OpenAI model list. |  -  |
**400** | Invalid request (OpenAI error envelope). On inference routes this includes &#x60;zero_data_retention_unavailable&#x60; when zero data retention is required and the model has no zero-data-retention host. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**402** | Insufficient balance (OpenAI error envelope, SERV-06). |  -  |
**403** | API key lacks the required scope (&#x60;insufficient_scope&#x60;), or, for &#x60;POST /fine_tuning/jobs&#x60;, GPU.ai can&#39;t provide this service in the caller&#39;s country or region (&#x60;region_not_supported&#x60;). OpenAI error envelope.  |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**502** | Internal server error (OpenAI error envelope). |  -  |
**503** | Upstream provider unavailable (OpenAI error envelope). Retry-After header may indicate seconds to wait. Code &#x60;data_retention_check_failed&#x60; means the org zero data retention setting could not be read, so the request was not sent; retry shortly. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_endpoints**
> EndpointList list_endpoints()

List model endpoints

Lists the organization's live model endpoints with their status, URL and machine counts. Requires the `functions:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.endpoint_list import EndpointList
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
    api_instance = gpuai_sdk.EndpointsApi(api_client)

    try:
        # List model endpoints
        api_response = api_instance.list_endpoints()
        print("The response of EndpointsApi->list_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->list_endpoints: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EndpointList**](EndpointList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization&#39;s endpoints. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

