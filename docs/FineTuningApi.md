# gpuai_sdk.FineTuningApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_fine_tuning_job**](FineTuningApi.md#cancel_fine_tuning_job) | **POST** /fine_tuning/jobs/{id}/cancel | Cancel a fine-tuning job (OpenAI-compatible)
[**create_file**](FineTuningApi.md#create_file) | **POST** /files | Upload a fine-tuning dataset file (OpenAI-compatible)
[**create_fine_tuning_job**](FineTuningApi.md#create_fine_tuning_job) | **POST** /fine_tuning/jobs | Create a managed fine-tuning job (OpenAI-compatible)
[**get_fine_tuning_job**](FineTuningApi.md#get_fine_tuning_job) | **GET** /fine_tuning/jobs/{id} | Retrieve a fine-tuning job (OpenAI-compatible)
[**list_fine_tuning_job_events**](FineTuningApi.md#list_fine_tuning_job_events) | **GET** /fine_tuning/jobs/{id}/events | List fine-tuning job events (OpenAI-compatible)
[**list_fine_tuning_jobs**](FineTuningApi.md#list_fine_tuning_jobs) | **GET** /fine_tuning/jobs | List fine-tuning jobs (OpenAI-compatible)


# **cancel_fine_tuning_job**
> FineTuningJob cancel_fine_tuning_job(id)

Cancel a fine-tuning job (OpenAI-compatible)

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.fine_tuning_job import FineTuningJob
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
    api_instance = gpuai_sdk.FineTuningApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel a fine-tuning job (OpenAI-compatible)
        api_response = api_instance.cancel_fine_tuning_job(id)
        print("The response of FineTuningApi->cancel_fine_tuning_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->cancel_fine_tuning_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FineTuningJob**](FineTuningJob.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cancelled fine-tuning job. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> FileObject create_file(purpose, file)

Upload a fine-tuning dataset file (OpenAI-compatible)

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.file_object import FileObject
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
    api_instance = gpuai_sdk.FineTuningApi(api_client)
    purpose = 'purpose_example' # str | 
    file = None # bytes | A JSONL chat-format training dataset.

    try:
        # Upload a fine-tuning dataset file (OpenAI-compatible)
        api_response = api_instance.create_file(purpose, file)
        print("The response of FineTuningApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purpose** | **str**|  | 
 **file** | **bytes**| A JSONL chat-format training dataset. | 

### Return type

[**FileObject**](FileObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The uploaded file object. |  -  |
**400** | Invalid request (OpenAI error envelope). |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**500** | Internal server error (OpenAI error envelope). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fine_tuning_job**
> FineTuningJob create_fine_tuning_job(create_fine_tuning_job_request)

Create a managed fine-tuning job (OpenAI-compatible)

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.create_fine_tuning_job_request import CreateFineTuningJobRequest
from gpuai_sdk.models.fine_tuning_job import FineTuningJob
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
    api_instance = gpuai_sdk.FineTuningApi(api_client)
    create_fine_tuning_job_request = gpuai_sdk.CreateFineTuningJobRequest() # CreateFineTuningJobRequest | 

    try:
        # Create a managed fine-tuning job (OpenAI-compatible)
        api_response = api_instance.create_fine_tuning_job(create_fine_tuning_job_request)
        print("The response of FineTuningApi->create_fine_tuning_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->create_fine_tuning_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_fine_tuning_job_request** | [**CreateFineTuningJobRequest**](CreateFineTuningJobRequest.md)|  | 

### Return type

[**FineTuningJob**](FineTuningJob.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created fine-tuning job. |  -  |
**400** | Invalid request (OpenAI error envelope). |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**402** | Insufficient balance (OpenAI error envelope, SERV-06). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**422** | Request validation failed (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**500** | Internal server error (OpenAI error envelope). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fine_tuning_job**
> FineTuningJob get_fine_tuning_job(id)

Retrieve a fine-tuning job (OpenAI-compatible)

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.fine_tuning_job import FineTuningJob
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
    api_instance = gpuai_sdk.FineTuningApi(api_client)
    id = 'id_example' # str | 

    try:
        # Retrieve a fine-tuning job (OpenAI-compatible)
        api_response = api_instance.get_fine_tuning_job(id)
        print("The response of FineTuningApi->get_fine_tuning_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->get_fine_tuning_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FineTuningJob**](FineTuningJob.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fine-tuning job. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fine_tuning_job_events**
> FineTuningJobEventList list_fine_tuning_job_events(id, after=after, limit=limit)

List fine-tuning job events (OpenAI-compatible)

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.fine_tuning_job_event_list import FineTuningJobEventList
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
    api_instance = gpuai_sdk.FineTuningApi(api_client)
    id = 'id_example' # str | 
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List fine-tuning job events (OpenAI-compatible)
        api_response = api_instance.list_fine_tuning_job_events(id, after=after, limit=limit)
        print("The response of FineTuningApi->list_fine_tuning_job_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->list_fine_tuning_job_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**FineTuningJobEventList**](FineTuningJobEventList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of fine-tuning job events. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**404** | Model or resource not found (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fine_tuning_jobs**
> FineTuningJobList list_fine_tuning_jobs(after=after, limit=limit)

List fine-tuning jobs (OpenAI-compatible)

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.fine_tuning_job_list import FineTuningJobList
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
    api_instance = gpuai_sdk.FineTuningApi(api_client)
    after = 'after_example' # str |  (optional)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List fine-tuning jobs (OpenAI-compatible)
        api_response = api_instance.list_fine_tuning_jobs(after=after, limit=limit)
        print("The response of FineTuningApi->list_fine_tuning_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FineTuningApi->list_fine_tuning_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**FineTuningJobList**](FineTuningJobList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of fine-tuning jobs. |  -  |
**401** | Missing or invalid API key (OpenAI error envelope). |  -  |
**403** | API key lacks the required scope (OpenAI error envelope). |  -  |
**429** | Rate limit exceeded (OpenAI error envelope). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

