# gpuai_sdk.FunctionsApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_function_version**](FunctionsApi.md#activate_function_version) | **POST** /functions/{id}/versions/{version_id}/activate | Confirm a version&#39;s upload and make it current
[**cancel_function_run**](FunctionsApi.md#cancel_function_run) | **POST** /functions/{id}/runs/{run_id}/cancel | Cancel a run
[**create_function**](FunctionsApi.md#create_function) | **POST** /functions | Get or create a function by name
[**create_function_run**](FunctionsApi.md#create_function_run) | **POST** /functions/{id}/runs | Call a function
[**create_function_version**](FunctionsApi.md#create_function_version) | **POST** /functions/{id}/versions | Register a version of a function
[**delete_function**](FunctionsApi.md#delete_function) | **DELETE** /functions/{id} | Delete a function
[**get_function**](FunctionsApi.md#get_function) | **GET** /functions/{id} | Get a function
[**get_function_run**](FunctionsApi.md#get_function_run) | **GET** /functions/{id}/runs/{run_id} | Get a run
[**get_function_run_logs**](FunctionsApi.md#get_function_run_logs) | **GET** /functions/{id}/runs/{run_id}/logs | Read a run&#39;s output
[**list_function_runs**](FunctionsApi.md#list_function_runs) | **GET** /functions/{id}/runs | List a function&#39;s runs
[**list_functions**](FunctionsApi.md#list_functions) | **GET** /functions | List functions


# **activate_function_version**
> FunctionVersion activate_function_version(id, version_id, idempotency_key=idempotency_key)

Confirm a version's upload and make it current

Reads the uploaded bundle back, checks it against the declared size and SHA-256 (422 on a mismatch or a missing upload), and makes the version the one the function's next call runs. Safe to repeat. Requires the `functions:write` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.function_version import FunctionVersion
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    id = 'id_example' # str | The function id.
    version_id = 'version_id_example' # str | The version id.
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Confirm a version's upload and make it current
        api_response = api_instance.activate_function_version(id, version_id, idempotency_key=idempotency_key)
        print("The response of FunctionsApi->activate_function_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->activate_function_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function id. | 
 **version_id** | **str**| The version id. | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**FunctionVersion**](FunctionVersion.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version is ready. |  -  |
**404** | No such function, version or run in the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_function_run**
> FunctionRun cancel_function_run(id, run_id, idempotency_key=idempotency_key)

Cancel a run

A queued run is cancelled at once; a running one is stopped on its machine within seconds, and the machine stays ready for the next call. Cancelling a finished run changes nothing and returns it, so the request is safe to repeat. Requires the `functions:write` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.function_run import FunctionRun
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    id = 'id_example' # str | The function id.
    run_id = 'run_id_example' # str | The run id.
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Cancel a run
        api_response = api_instance.cancel_function_run(id, run_id, idempotency_key=idempotency_key)
        print("The response of FunctionsApi->cancel_function_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->cancel_function_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function id. | 
 **run_id** | **str**| The run id. | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**FunctionRun**](FunctionRun.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The run after the request. |  -  |
**404** | No such function, version or run in the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_function**
> Function create_function(create_function_request, idempotency_key=idempotency_key)

Get or create a function by name

Returns the organization's function with this name, creating it on first use (201) or returning the existing one (200). Creating a function starts no machine and costs nothing. Requires the `functions:write` scope. The key must belong to a user, because the function's machines are launched as that user.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.create_function_request import CreateFunctionRequest
from gpuai_sdk.models.function import Function
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    create_function_request = gpuai_sdk.CreateFunctionRequest() # CreateFunctionRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Get or create a function by name
        api_response = api_instance.create_function(create_function_request, idempotency_key=idempotency_key)
        print("The response of FunctionsApi->create_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->create_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_function_request** | [**CreateFunctionRequest**](CreateFunctionRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**Function**](Function.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | &#x60;region_not_supported&#x60; — GPU.ai can&#39;t provide this service in the caller&#39;s country or region. Returned only for new spending (launches, deposits, key minting); reading, stopping and deleting resources are never refused, and support stays reachable.  |  -  |
**200** | The function already existed. |  -  |
**201** | Created. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_function_run**
> FunctionRun create_function_run(id, create_function_run_request, idempotency_key=idempotency_key)

Call a function

Queues one call and returns at once (202). A warm machine takes it within moments; otherwise a machine is started for it, up to the function's `max_concurrency`, beyond which calls wait in the queue. Read the run with `wait` for the outcome. Send an `Idempotency-Key` so a retried request does not run the function twice. Calling a function can start a billed machine: an organization with no balance is refused with 402, and the organization's spending limits apply when the machine is requested. Requires the `functions:write` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.create_function_run_request import CreateFunctionRunRequest
from gpuai_sdk.models.function_run import FunctionRun
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    id = 'id_example' # str | The function id.
    create_function_run_request = gpuai_sdk.CreateFunctionRunRequest() # CreateFunctionRunRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Call a function
        api_response = api_instance.create_function_run(id, create_function_run_request, idempotency_key=idempotency_key)
        print("The response of FunctionsApi->create_function_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->create_function_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function id. | 
 **create_function_run_request** | [**CreateFunctionRunRequest**](CreateFunctionRunRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**FunctionRun**](FunctionRun.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | &#x60;region_not_supported&#x60; — GPU.ai can&#39;t provide this service in the caller&#39;s country or region. Returned only for new spending (launches, deposits, key minting); reading, stopping and deleting resources are never refused, and support stays reachable.  |  -  |
**202** | The call is queued. |  -  |
**402** | The organization has no balance. |  -  |
**404** | No such function, version or run in the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_function_version**
> FunctionVersion create_function_version(id, create_function_version_request, idempotency_key=idempotency_key)

Register a version of a function

Declares one version of the function: the digest of its pickled code, its Python dependencies and its settings. Idempotent on `content_hash`: the same hash returns the existing version (200) instead of a new one (201). A version whose code is not uploaded yet carries an `upload` URL; PUT the bundle there, then activate the version. Requires the `functions:write` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.create_function_version_request import CreateFunctionVersionRequest
from gpuai_sdk.models.function_version import FunctionVersion
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    id = 'id_example' # str | The function id.
    create_function_version_request = gpuai_sdk.CreateFunctionVersionRequest() # CreateFunctionVersionRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Register a version of a function
        api_response = api_instance.create_function_version(id, create_function_version_request, idempotency_key=idempotency_key)
        print("The response of FunctionsApi->create_function_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->create_function_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function id. | 
 **create_function_version_request** | [**CreateFunctionVersionRequest**](CreateFunctionVersionRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**FunctionVersion**](FunctionVersion.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | &#x60;region_not_supported&#x60; — GPU.ai can&#39;t provide this service in the caller&#39;s country or region. Returned only for new spending (launches, deposits, key minting); reading, stopping and deleting resources are never refused, and support stays reachable.  |  -  |
**200** | A version with this content hash already existed. |  -  |
**201** | Created. |  -  |
**404** | No such function, version or run in the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_function**
> delete_function(id)

Delete a function

The function stops taking calls, its queued calls are cancelled, a call that is executing is stopped, and its machines are released, which ends their billing. The name can be reused afterwards. Requires the `functions:write` scope.

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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    id = 'id_example' # str | The function id.

    try:
        # Delete a function
        api_instance.delete_function(id)
    except Exception as e:
        print("Exception when calling FunctionsApi->delete_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function id. | 

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
**404** | No such function, version or run in the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function**
> Function get_function(id)

Get a function

Requires the `functions:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.function import Function
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    id = 'id_example' # str | The function id.

    try:
        # Get a function
        api_response = api_instance.get_function(id)
        print("The response of FunctionsApi->get_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function id. | 

### Return type

[**Function**](Function.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No such function, version or run in the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_run**
> FunctionRun get_function_run(id, run_id, wait=wait, include_result=include_result)

Get a run

Returns one call. With `wait`, the request is held until the run finishes or the wait elapses, so a caller blocks on one request instead of polling. Requires the `functions:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.function_run import FunctionRun
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    id = 'id_example' # str | The function id.
    run_id = 'run_id_example' # str | The run id.
    wait = 56 # int | Seconds to hold the request while the run is not finished. (optional)
    include_result = True # bool | Include the pickled return value of a succeeded run. (optional)

    try:
        # Get a run
        api_response = api_instance.get_function_run(id, run_id, wait=wait, include_result=include_result)
        print("The response of FunctionsApi->get_function_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function id. | 
 **run_id** | **str**| The run id. | 
 **wait** | **int**| Seconds to hold the request while the run is not finished. | [optional] 
 **include_result** | **bool**| Include the pickled return value of a succeeded run. | [optional] 

### Return type

[**FunctionRun**](FunctionRun.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No such function, version or run in the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_run_logs**
> FunctionRunLogs get_function_run_logs(id, run_id, after=after, limit=limit, wait=wait)

Read a run's output

Returns the run's stdout and stderr after `after`, oldest first. With `wait`, the request is held until there is new output or the run finishes, which is how a client follows a live run. Up to 4 MB of output is kept per run. Requires the `functions:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.function_run_logs import FunctionRunLogs
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    id = 'id_example' # str | The function id.
    run_id = 'run_id_example' # str | The run id.
    after = 56 # int | Return chunks after this cursor. Omit to read from the start. (optional)
    limit = 1000 # int |  (optional) (default to 1000)
    wait = 56 # int | Seconds to hold the request while there is nothing new. (optional)

    try:
        # Read a run's output
        api_response = api_instance.get_function_run_logs(id, run_id, after=after, limit=limit, wait=wait)
        print("The response of FunctionsApi->get_function_run_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_run_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function id. | 
 **run_id** | **str**| The run id. | 
 **after** | **int**| Return chunks after this cursor. Omit to read from the start. | [optional] 
 **limit** | **int**|  | [optional] [default to 1000]
 **wait** | **int**| Seconds to hold the request while there is nothing new. | [optional] 

### Return type

[**FunctionRunLogs**](FunctionRunLogs.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No such function, version or run in the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_function_runs**
> FunctionRunList list_function_runs(id, cursor=cursor, limit=limit)

List a function's runs

Newest first. Requires the `functions:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.function_run_list import FunctionRunList
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)
    id = 'id_example' # str | The function id.
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List a function's runs
        api_response = api_instance.list_function_runs(id, cursor=cursor, limit=limit)
        print("The response of FunctionsApi->list_function_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->list_function_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The function id. | 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**FunctionRunList**](FunctionRunList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No such function, version or run in the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_functions**
> FunctionList list_functions()

List functions

Returns the organization's functions, newest first, each with the settings of its current version, what its machines are doing and what it cost in the last 24 hours. Requires the `functions:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.function_list import FunctionList
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
    api_instance = gpuai_sdk.FunctionsApi(api_client)

    try:
        # List functions
        api_response = api_instance.list_functions()
        print("The response of FunctionsApi->list_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->list_functions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FunctionList**](FunctionList.md)

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

