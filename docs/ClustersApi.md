# gpuai_sdk.ClustersApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /clusters | Create a cluster
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /clusters/{id} | Delete a cluster
[**delete_cluster_queue**](ClustersApi.md#delete_cluster_queue) | **DELETE** /clusters/{id}/queues/{name} | Delete a scheduler queue
[**get_cluster**](ClustersApi.md#get_cluster) | **GET** /clusters/{id} | Get a cluster
[**get_cluster_kubeconfig**](ClustersApi.md#get_cluster_kubeconfig) | **GET** /clusters/{id}/kubeconfig | Get a kubeconfig for a cluster
[**kubernetes_proxy_get**](ClustersApi.md#kubernetes_proxy_get) | **GET** /clusters/{id}/kubernetes/{path} | Kubernetes API (GET)
[**kubernetes_proxy_post**](ClustersApi.md#kubernetes_proxy_post) | **POST** /clusters/{id}/kubernetes/{path} | Kubernetes API (POST)
[**list_cluster_gpu_types**](ClustersApi.md#list_cluster_gpu_types) | **GET** /clusters/gpu-types | List the machines clusters can start now
[**list_cluster_queues**](ClustersApi.md#list_cluster_queues) | **GET** /clusters/{id}/queues | List a cluster&#39;s scheduler queues
[**list_clusters**](ClustersApi.md#list_clusters) | **GET** /clusters | List clusters
[**ray_proxy_get**](ClustersApi.md#ray_proxy_get) | **GET** /clusters/{id}/ray/{path} | Ray dashboard and job API (GET)
[**ray_proxy_post**](ClustersApi.md#ray_proxy_post) | **POST** /clusters/{id}/ray/{path} | Ray dashboard and job API (POST)
[**resize_cluster**](ClustersApi.md#resize_cluster) | **PATCH** /clusters/{id} | Resize a cluster
[**set_cluster_queue**](ClustersApi.md#set_cluster_queue) | **PUT** /clusters/{id}/queues/{name} | Create or update a scheduler queue


# **create_cluster**
> Cluster create_cluster(cluster_create)

Create a cluster

Creates a cluster of GPU machines joined on an encrypted private network (WireGuard) as one Kubernetes cluster, with Ray (KubeRay) and the KAI scheduler (NVIDIA's open-source Run:ai scheduler) installed. GPU.ai rents `min_nodes` machines right away and adds machines when work waits for GPUs, up to `max_nodes`; a machine with no GPU work for `idle_timeout` seconds is removed, down to `min_nodes`. Each machine is billed like an instance. `placement` "spread" places machines on different suppliers where it can. Returns 422 `validation_failed` for a bad field, 409 `name_taken` for a duplicate name, 409 `limit_reached` at the per-organization cap, and 402 `insufficient_balance` when the prepaid balance is not positive (a cluster whose balance runs out later starts no machines until credit is added). Returns 409 `no_capacity`, with the nearest machine in stock as `alternative`, when no cluster supplier has the machine (in the requested regions) now; see GET /clusters/gpu-types. Also 409 `no_capacity` when the machine is in stock but every listing costs more than `max_price_per_hour`; the detail names the cheapest price. Clusters are for work that splits into independent pieces: batch inference, hyperparameter sweeps, evaluations and data processing. They are not for training one model across several machines, because the links between machines are slow. Requires the `instances:write` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.cluster import Cluster
from gpuai_sdk.models.cluster_create import ClusterCreate
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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    cluster_create = gpuai_sdk.ClusterCreate() # ClusterCreate | 

    try:
        # Create a cluster
        api_response = api_instance.create_cluster(cluster_create)
        print("The response of ClustersApi->create_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_create** | [**ClusterCreate**](ClusterCreate.md)|  | 

### Return type

[**Cluster**](Cluster.md)

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

# **delete_cluster**
> delete_cluster(id)

Delete a cluster

Deletes the cluster. Every machine is terminated within seconds and stops billing when terminated; the cost stays in your usage. Requires the `instances:write` scope.

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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.

    try:
        # Delete a cluster
        api_instance.delete_cluster(id)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 

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

# **delete_cluster_queue**
> delete_cluster_queue(id, name)

Delete a scheduler queue

Deletes a queue. The default queue cannot be deleted. Requires the `instances:write` scope.

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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.
    name = 'name_example' # str | The queue's name (lowercase letters, digits and hyphens).

    try:
        # Delete a scheduler queue
        api_instance.delete_cluster_queue(id, name)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 
 **name** | **str**| The queue&#39;s name (lowercase letters, digits and hyphens). | 

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
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> Cluster get_cluster(id)

Get a cluster

Returns one cluster with its machines, scheduler queues, the queued and running GPU work the head machine last reported, and the cost so far. Requires the `instances:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.cluster import Cluster
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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.

    try:
        # Get a cluster
        api_response = api_instance.get_cluster(id)
        print("The response of ClustersApi->get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cluster. |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_kubeconfig**
> str get_cluster_kubeconfig(id)

Get a kubeconfig for a cluster

A kubeconfig whose server is the cluster's Kubernetes API through GPU.ai and whose token is the API key of this request. Requires the `instances:read` scope; kubectl itself needs `instances:write`. The console's download carries a short-lived credential instead (a `gpuai_kc_` token valid for 8 hours, for this cluster and the signed-in user only), which the Kubernetes route accepts in place of an API key. 404 for an unknown or deleted cluster.

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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.

    try:
        # Get a kubeconfig for a cluster
        api_response = api_instance.get_cluster_kubeconfig(id)
        print("The response of ClustersApi->get_cluster_kubeconfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_kubeconfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The kubeconfig. |  -  |
**404** | Error response (RFC 7807) |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_proxy_get**
> kubernetes_proxy_get(id, path)

Kubernetes API (GET)

Forwards to the cluster's Kubernetes API with full rights in the cluster. Use it through kubectl with the kubeconfig from `/clusters/{id}/kubeconfig`. Every method is forwarded; GET and POST are listed. Exec and attach are not available. Requires the `instances:write` scope.

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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.
    path = 'path_example' # str | Any Kubernetes API path, such as api/v1/pods.

    try:
        # Kubernetes API (GET)
        api_instance.kubernetes_proxy_get(id, path)
    except Exception as e:
        print("Exception when calling ClustersApi->kubernetes_proxy_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 
 **path** | **str**| Any Kubernetes API path, such as api/v1/pods. | 

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
**200** | The Kubernetes API&#39;s answer. |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_proxy_post**
> kubernetes_proxy_post(id, path)

Kubernetes API (POST)

Forwards to the cluster's Kubernetes API (see GET).

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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.
    path = 'path_example' # str | Any Kubernetes API path, such as api/v1/pods.

    try:
        # Kubernetes API (POST)
        api_instance.kubernetes_proxy_post(id, path)
    except Exception as e:
        print("Exception when calling ClustersApi->kubernetes_proxy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 
 **path** | **str**| Any Kubernetes API path, such as api/v1/pods. | 

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
**200** | The Kubernetes API&#39;s answer. |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_gpu_types**
> GPUStockList list_cluster_gpu_types()

List the machines clusters can start now

The GPU machines the cluster suppliers can start now, by GPU type and GPUs per machine (1, 2, 4 or 8), in stock first and cheapest first, with the regions that have stock. A create on a machine with nothing in stock is refused with 409 `no_capacity`, naming the nearest machine in stock in `alternative`. Requires the `instances:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.gpu_stock_list import GPUStockList
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
    api_instance = gpuai_sdk.ClustersApi(api_client)

    try:
        # List the machines clusters can start now
        api_response = api_instance.list_cluster_gpu_types()
        print("The response of ClustersApi->list_cluster_gpu_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_cluster_gpu_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GPUStockList**](GPUStockList.md)

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
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_queues**
> ClusterQueueList list_cluster_queues(id)

List a cluster's scheduler queues

Lists the KAI scheduler queues with their priority, GPU quota and limit, and the GPUs each uses and has waiting. Requires the `instances:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.cluster_queue_list import ClusterQueueList
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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.

    try:
        # List a cluster's scheduler queues
        api_response = api_instance.list_cluster_queues(id)
        print("The response of ClustersApi->list_cluster_queues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_cluster_queues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 

### Return type

[**ClusterQueueList**](ClusterQueueList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queues. |  -  |
**404** | Error response (RFC 7807) |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clusters**
> ClusterList list_clusters()

List clusters

Lists the organization's clusters (and deleted ones whose machines are still being released) with status, machine counts and cost so far. Requires the `instances:read` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.cluster_list import ClusterList
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
    api_instance = gpuai_sdk.ClustersApi(api_client)

    try:
        # List clusters
        api_response = api_instance.list_clusters()
        print("The response of ClustersApi->list_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_clusters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterList**](ClusterList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The organization&#39;s clusters. |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ray_proxy_get**
> object ray_proxy_get(id, path)

Ray dashboard and job API (GET)

Forwards to the cluster's Ray dashboard. Use `https://api.gpu.ai/v1/clusters/{id}/ray` as the address of `ray job submit` with the API key in an Authorization header. Every method is forwarded; GET and POST are listed. In Ray's job API, `api/jobs/` lists the jobs, `api/jobs/{submission_id}` reads one and `api/jobs/{submission_id}/logs` returns its log, which Ray collects from every machine. Returns 503 `cluster_not_ready` until the head machine is up. Requires the `instances:write` scope.

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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.
    path = 'path_example' # str | Any Ray dashboard or job API path, such as api/jobs/.

    try:
        # Ray dashboard and job API (GET)
        api_response = api_instance.ray_proxy_get(id, path)
        print("The response of ClustersApi->ray_proxy_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->ray_proxy_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 
 **path** | **str**| Any Ray dashboard or job API path, such as api/jobs/. | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Ray dashboard&#39;s answer, JSON for the job API. |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ray_proxy_post**
> object ray_proxy_post(id, path, request_body=request_body)

Ray dashboard and job API (POST)

Forwards to the cluster's Ray dashboard (see GET). POST `api/jobs/` with a body such as `{"entrypoint": "python batch.py", "runtime_env": {"pip": ["vllm"]}}` submits a job and returns its `submission_id`; POST `api/jobs/{submission_id}/stop` stops it.

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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.
    path = 'path_example' # str | Any Ray dashboard or job API path, such as api/jobs/.
    request_body = None # Dict[str, Optional[object]] |  (optional)

    try:
        # Ray dashboard and job API (POST)
        api_response = api_instance.ray_proxy_post(id, path, request_body=request_body)
        print("The response of ClustersApi->ray_proxy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->ray_proxy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 
 **path** | **str**| Any Ray dashboard or job API path, such as api/jobs/. | 
 **request_body** | [**Dict[str, Optional[object]]**](object.md)|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Ray dashboard&#39;s answer, JSON for the job API. |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_cluster**
> Cluster resize_cluster(id, cluster_resize)

Resize a cluster

Changes the minimum or maximum number of machines or the idle period. Machines are added within seconds when `min_nodes` rises; machines over a lowered `max_nodes` are drained and released. Returns 409 `cluster_deleting` for a cluster being deleted. Requires the `instances:write` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.cluster import Cluster
from gpuai_sdk.models.cluster_resize import ClusterResize
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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.
    cluster_resize = gpuai_sdk.ClusterResize() # ClusterResize | 

    try:
        # Resize a cluster
        api_response = api_instance.resize_cluster(id, cluster_resize)
        print("The response of ClustersApi->resize_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->resize_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 
 **cluster_resize** | [**ClusterResize**](ClusterResize.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The resized cluster. |  -  |
**404** | Error response (RFC 7807) |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cluster_queue**
> ClusterQueue set_cluster_queue(id, name, cluster_queue_set)

Create or update a scheduler queue

Sets a queue. Pods choose it with the label `kai.scheduler/queue` and `schedulerName: kai-scheduler`. `gpu_quota` is the GPUs the queue is guaranteed and `gpu_limit` the most it may use (-1 for none); work over the limit waits until the queue's own work frees GPUs, and adds no machines. Requires the `instances:write` scope.

### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.cluster_queue import ClusterQueue
from gpuai_sdk.models.cluster_queue_set import ClusterQueueSet
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
    api_instance = gpuai_sdk.ClustersApi(api_client)
    id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The cluster's id.
    name = 'name_example' # str | The queue's name (lowercase letters, digits and hyphens).
    cluster_queue_set = gpuai_sdk.ClusterQueueSet() # ClusterQueueSet | 

    try:
        # Create or update a scheduler queue
        api_response = api_instance.set_cluster_queue(id, name, cluster_queue_set)
        print("The response of ClustersApi->set_cluster_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->set_cluster_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The cluster&#39;s id. | 
 **name** | **str**| The queue&#39;s name (lowercase letters, digits and hyphens). | 
 **cluster_queue_set** | [**ClusterQueueSet**](ClusterQueueSet.md)|  | 

### Return type

[**ClusterQueue**](ClusterQueue.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queue. |  -  |
**404** | Error response (RFC 7807) |  -  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

