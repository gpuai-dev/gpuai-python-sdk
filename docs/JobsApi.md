# gpuai_sdk.JobsApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](JobsApi.md#cancel_job) | **POST** /jobs/{id}/cancel | Cancel a job
[**create_job**](JobsApi.md#create_job) | **POST** /jobs | Submit a job
[**create_job_input**](JobsApi.md#create_job_input) | **POST** /jobs/inputs | Upload a file for a job to read
[**get_job**](JobsApi.md#get_job) | **GET** /jobs/{id} | Get a job
[**get_job_logs**](JobsApi.md#get_job_logs) | **GET** /jobs/{id}/logs | Read a job&#39;s output
[**get_job_outputs**](JobsApi.md#get_job_outputs) | **GET** /jobs/{id}/outputs | Download what a job wrote to /outputs
[**get_job_telemetry**](JobsApi.md#get_job_telemetry) | **GET** /jobs/{id}/telemetry | Read a job&#39;s GPU memory telemetry
[**get_job_trial**](JobsApi.md#get_job_trial) | **GET** /jobs/trial | Whether this organization&#39;s first jobs are free
[**list_job_gpu_types**](JobsApi.md#list_job_gpu_types) | **GET** /jobs/gpu-types | List the GPU types a job can run on
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /jobs | List jobs


# **cancel_job**
> Job cancel_job(id, idempotency_key=idempotency_key)

Cancel a job

Cancels a job. A queued job is cancelled at once. A running job is stopped the next time its machine reports, within a few seconds, and shows `cancel_requested` until then. Cancelling a job that has already finished returns it unchanged. Requires the `instances:write` scope.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job import Job
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
    api_instance = gpuai_sdk.JobsApi(api_client)
    id = 'id_example' # str | The job id.
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Cancel a job
        api_response = api_instance.cancel_job(id, idempotency_key=idempotency_key)
        print("The response of JobsApi->cancel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->cancel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The job id. | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The job after the cancel request. |  -  |
**404** | The job does not exist or is not owned by the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> Job create_job(job_create, idempotency_key=idempotency_key)

Submit a job

Queues a batch job: a container image, a command, and the GPU it needs. The platform places it on a machine in your organization's job pool, starting a machine when none has room, and terminates machines that have been empty for a few minutes. Requires the `instances:write` scope, because a job can start a machine.

Three opt-ins decide how the job is placed. `max_wait_seconds` lets the job wait for space on a machine you are already paying for before a new one is started. `allow_sharing` lets the job run on the same GPU as other jobs from your own organization. A GPU is never shared with another customer. `allow_restart` lets the platform stop and rerun the job, which sharing needs.

A job shares a GPU only when `allow_sharing` and `allow_restart` are both true and its memory is known, from `memory_hint_mb` or from the peaks of earlier finished jobs with the same name or image. Any other job gets a whole GPU.

Sharing is also limited by compute. Jobs share a GPU only while the sum of their expected compute duties (the share of time each keeps the GPU busy) stays at or under 100%, so two jobs that saturate the GPU never share one. A job's duty comes from `compute_hint_pct` or from the measured utilization of earlier finished jobs with the same name or image. A job with neither counts as 100% and gets a GPU to itself until it has been measured.

The memory reservation is not a hard cap. A job that exits out of GPU memory, or that is stopped for outgrowing its reservation on a full GPU, is run again with a larger reservation, then with a whole GPU, up to `max_retries`. Every job gets a checkpoint directory that survives those reruns on the same machine.

Billing: the machines a job runs on are instances of your organization and are billed like any instance. `attributed_cost_usd` on the job is its share of that, for display.

Free trial: when this deployment runs one, an organization's first jobs are free up to a cap (GET /jobs/trial). Their attributed cost is credited back to the balance as they run.

No balance: an organization with no balance is refused (402) unless the deployment runs the free trial for organizations with no balance and GET /jobs/trial reports `funding` "no_deposit". Then the job runs on the trial with `trial_funded` true. When the trial credit is used the job is cancelled with the status reason "Stopped because your free Jobs trial credit ran out. Add credits to keep running jobs."


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job import Job
from gpuai_sdk.models.job_create import JobCreate
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
    api_instance = gpuai_sdk.JobsApi(api_client)
    job_create = gpuai_sdk.JobCreate() # JobCreate | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Submit a job
        api_response = api_instance.create_job(job_create, idempotency_key=idempotency_key)
        print("The response of JobsApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_create** | [**JobCreate**](JobCreate.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * GPUAI-Hint - Advisory only. Sent while the organization&#39;s first jobs are free (GET /jobs/trial), e.g. \&quot;Your first jobs are free, up to $10. We credit back what they cost as they run.\&quot; For a job that runs on the trial with no balance it says the job stops when the trial credit is used. <br>  |
**402** | The organization has no balance and the job cannot run on the free trial (the trial is off, used, or at its limit for today, or the person already used it). The detail says which. Add credits, then submit again.  |  -  |
**422** | Validation failed. The detail names the field: a missing image or command, an unknown field, an unknown &#x60;gpu_type&#x60;, neither &#x60;gpu_type&#x60; nor &#x60;min_vram_gb&#x60;, a memory hint larger than the GPU, an environment variable name starting with &#x60;GPUAI_&#x60;, or a value out of range.  |  -  |
**429** | Rate limited, or the organization already has the maximum number of queued and running jobs.  |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_input**
> JobInput create_job_input(job_input_create)

Upload a file for a job to read

Returns a URL to PUT one file to, in a single request of exactly `bytes` bytes, within an hour. Name the returned `id` in the `input_file` of POST /jobs. The job reads the file from `GPUAI_INPUT_URL`. A file no job has read is deleted after 7 days. Requires the `instances:write` scope.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job_input import JobInput
from gpuai_sdk.models.job_input_create import JobInputCreate
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
    api_instance = gpuai_sdk.JobsApi(api_client)
    job_input_create = gpuai_sdk.JobInputCreate() # JobInputCreate | 

    try:
        # Upload a file for a job to read
        api_response = api_instance.create_job_input(job_input_create)
        print("The response of JobsApi->create_job_input:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job_input: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_input_create** | [**JobInputCreate**](JobInputCreate.md)|  | 

### Return type

[**JobInput**](JobInput.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Job files are not enabled on this deployment. |  -  |
**422** | The file name is empty or the size is above &#x60;max_bytes&#x60;. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> Job get_job(id)

Get a job

Returns one job with its attempts. Requires the `instances:read` scope.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job import Job
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
    api_instance = gpuai_sdk.JobsApi(api_client)
    id = 'id_example' # str | The job id.

    try:
        # Get a job
        api_response = api_instance.get_job(id)
        print("The response of JobsApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The job does not exist or is not owned by the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_logs**
> JobLogs get_job_logs(id, after=after, limit=limit)

Read a job's output

Returns the job's combined standard output and standard error, in chunks, across all attempts. Pass the `next_after` of one response as `after` on the next to read on from there. Output is uploaded every few seconds while the job runs, and stored output is capped at about 8 MB per attempt. Requires the `instances:read` scope.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job_logs import JobLogs
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
    api_instance = gpuai_sdk.JobsApi(api_client)
    id = 'id_example' # str | The job id.
    after = 0 # int | Return chunks after this chunk id. (optional) (default to 0)
    limit = 100 # int | Maximum number of chunks to return. (optional) (default to 100)

    try:
        # Read a job's output
        api_response = api_instance.get_job_logs(id, after=after, limit=limit)
        print("The response of JobsApi->get_job_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The job id. | 
 **after** | **int**| Return chunks after this chunk id. | [optional] [default to 0]
 **limit** | **int**| Maximum number of chunks to return. | [optional] [default to 100]

### Return type

[**JobLogs**](JobLogs.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The job does not exist or is not owned by the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_outputs**
> JobOutputs get_job_outputs(id)

Download what a job wrote to /outputs

Everything a job writes to its outputs directory (`/outputs`, also in `GPUAI_OUTPUTS_DIR`) is zipped and stored when the job ends, up to `max_bytes`. `status` is `available` (download the zip from `url` until `url_expires_at`, then ask again for a fresh URL), `pending` (the job has not ended), `none` (it wrote no files) or `expired` (stored files are kept for 7 days). A retried job keeps the outputs of its last attempt. Requires the `instances:read` scope.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job_outputs import JobOutputs
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
    api_instance = gpuai_sdk.JobsApi(api_client)
    id = 'id_example' # str | The job id.

    try:
        # Download what a job wrote to /outputs
        api_response = api_instance.get_job_outputs(id)
        print("The response of JobsApi->get_job_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_outputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The job id. | 

### Return type

[**JobOutputs**](JobOutputs.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The job does not exist, is not owned by the caller&#39;s organization, or job files are off. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_telemetry**
> JobTelemetry get_job_telemetry(id)

Read a job's GPU memory telemetry

Returns the job's peak GPU memory, its reservation, and up to the 720 most recent memory points. The machine samples every 2 seconds and stores one point per report, the highest sample in that window. Points are kept for 30 days. Requires the `instances:read` scope.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job_telemetry import JobTelemetry
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
    api_instance = gpuai_sdk.JobsApi(api_client)
    id = 'id_example' # str | The job id.

    try:
        # Read a job's GPU memory telemetry
        api_response = api_instance.get_job_telemetry(id)
        print("The response of JobsApi->get_job_telemetry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_telemetry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The job id. | 

### Return type

[**JobTelemetry**](JobTelemetry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | The job does not exist or is not owned by the caller&#39;s organization. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_trial**
> JobTrial get_job_trial()

Whether this organization's first jobs are free

Reports the Jobs free trial for this organization. When the deployment runs one, an organization's first jobs are free up to `cap_cents`: the cost attributed to its jobs is credited back to its balance as they run, until the credits reach the cap. One trial per organization, for organizations that had not used Jobs before the trial started. `enabled` is false when there is no trial. Requires the `instances:read` scope.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job_trial import JobTrial
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
    api_instance = gpuai_sdk.JobsApi(api_client)

    try:
        # Whether this organization's first jobs are free
        api_response = api_instance.get_job_trial()
        print("The response of JobsApi->get_job_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_trial: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JobTrial**](JobTrial.md)

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

# **list_job_gpu_types**
> JobGpuTypes list_job_gpu_types()

List the GPU types a job can run on

Returns the GPU types the suppliers that run jobs rent as a one-GPU machine, smallest memory first. A type is listed when one of them offered it in the last 7 days, in stock or not. `available_now` says whether one has such a machine to rent now, and `price_per_gpu_hour` is the cheapest retail price of it at that read (a guide, not a quote: the launch prices it again). When `complete` is true, `POST /jobs` refuses any other `gpu_type` with a 422 (and a `min_vram_gb` larger than every listed type), instead of queueing a job that could never start. When `complete` is false the list may be partial or empty, and a job for any known GPU model is accepted and waits for a machine. Requires the `instances:read` scope.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job_gpu_types import JobGpuTypes
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
    api_instance = gpuai_sdk.JobsApi(api_client)

    try:
        # List the GPU types a job can run on
        api_response = api_instance.list_job_gpu_types()
        print("The response of JobsApi->list_job_gpu_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_job_gpu_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JobGpuTypes**](JobGpuTypes.md)

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

# **list_jobs**
> JobPage list_jobs(status=status, cursor=cursor, limit=limit)

List jobs

Lists this organization's jobs, newest first. Requires the `instances:read` scope. Jobs belonging to other organizations are never returned.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.job_page import JobPage
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
    api_instance = gpuai_sdk.JobsApi(api_client)
    status = 'status_example' # str | Only return jobs in this status. (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List jobs
        api_response = api_instance.list_jobs(status=status, cursor=cursor, limit=limit)
        print("The response of JobsApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Only return jobs in this status. | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**JobPage**](JobPage.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Validation failed, such as an unknown status or an invalid cursor. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

