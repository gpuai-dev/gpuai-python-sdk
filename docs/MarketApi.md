# gpuai_sdk.MarketApi

All URIs are relative to *https://api.gpu.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_market_history**](MarketApi.md#get_market_history) | **GET** /market-history | Get a GPU&#39;s price and availability over time


# **get_market_history**
> MarketHistoryResponse get_market_history(gpu_model, region=region, capacity_class=capacity_class, bucket=bucket, var_from=var_from, to=to)

Get a GPU's price and availability over time

Returns GPU.ai's own price and obtainable capacity for one GPU model over a window, at 15-minute or daily resolution. Requires the `market:read` scope (or `full_access`).

THE NULL CONTRACT. `price_per_gpu_hour` and `available_count` are nullable, and the two states are different facts that must not be collapsed:

* a real `0` means we sampled that bucket and the market was sold out;
* `null` means we did NOT sample that bucket — a failed poll, a skipped cycle, an incident on our side. It says nothing about supply.

The response materializes the full bucket grid across the window, so a gap has visible width. Do not interpolate across a null: that asserts a continuity the data does not have, and reading one as a zero reports our own outages as supplier stockouts.

PER-GPU NORMALIZATION. `price_per_gpu_hour` is always a per-GPU rate. When it was divided out of a whole-node price, `node_price_per_hour` and `gpu_count` are present and describe that derivation; they are absent for single-GPU capacity. A per-GPU figure presented without that context implies single-GPU rentability that whole-node capacity does not offer.

WINDOW CAPS. `bucket=1d` is capped at 365 days (the retention window). `bucket=15m` is capped at 90 days when BOTH `region` and `capacity_class` are supplied, and at 31 days when either is omitted, because an unscoped 15-minute series scans every region and class in every bucket. An over-wide window is a 400 naming the cap and both escapes, never a silent truncation.

This series carries no upstream supplier identity of any kind: the price is GPU.ai's own floor and the count is an aggregate.


### Example

* Bearer (gpuai_live_<24-base62>) Authentication (bearerAuth):

```python
import gpuai_sdk
from gpuai_sdk.models.market_history_response import MarketHistoryResponse
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
    api_instance = gpuai_sdk.MarketApi(api_client)
    gpu_model = 'gpu_model_example' # str | GPU model to chart, e.g. \"H100\". Required — it is the leading column of the lookup index.
    region = 'region_example' # str | Canonical region to narrow the series to. Omit to MERGE every region rather than to filter on the empty string. (optional)
    capacity_class = 'capacity_class_example' # str | Capacity class to narrow the series to. Omit to merge both. (optional)
    bucket = '15m' # str | Resolution. Only these two values are accepted: the series cannot be returned finer than it was stored. (optional) (default to '15m')
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Start of the window (RFC3339). Defaults to 7 days before `to`. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | End of the window (RFC3339). Defaults to now; a future value is clamped to now, since no bucket can exist for a time that has not happened. (optional)

    try:
        # Get a GPU's price and availability over time
        api_response = api_instance.get_market_history(gpu_model, region=region, capacity_class=capacity_class, bucket=bucket, var_from=var_from, to=to)
        print("The response of MarketApi->get_market_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketApi->get_market_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpu_model** | **str**| GPU model to chart, e.g. \&quot;H100\&quot;. Required — it is the leading column of the lookup index. | 
 **region** | **str**| Canonical region to narrow the series to. Omit to MERGE every region rather than to filter on the empty string. | [optional] 
 **capacity_class** | **str**| Capacity class to narrow the series to. Omit to merge both. | [optional] 
 **bucket** | **str**| Resolution. Only these two values are accepted: the series cannot be returned finer than it was stored. | [optional] [default to &#39;15m&#39;]
 **var_from** | **datetime**| Start of the window (RFC3339). Defaults to 7 days before &#x60;to&#x60;. | [optional] 
 **to** | **datetime**| End of the window (RFC3339). Defaults to now; a future value is clamped to now, since no bucket can exist for a time that has not happened. | [optional] 

### Return type

[**MarketHistoryResponse**](MarketHistoryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Validation failed — a missing &#x60;gpu_model&#x60;, a non-canonical region, an unknown &#x60;capacity_class&#x60; or &#x60;bucket&#x60;, a non-RFC3339 timestamp, a &#x60;from&#x60; that is not before &#x60;to&#x60;, or a window wider than the cap for the requested resolution and scope. The detail names the cap and both ways to stay under it.  |  -  |
**429** | Rate limit exceeded (RFC 7807). Retry-After header indicates seconds to wait. |  * Retry-After - Seconds the client should wait before retrying. <br>  |
**0** | Error response (RFC 7807) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

