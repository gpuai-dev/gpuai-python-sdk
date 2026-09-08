# MarketHistoryPoint

One bucket of a price/stock series.  The nullability of `price_per_gpu_hour` and `available_count` is the contract, not a convenience: a real 0 is a bucket we sampled and found sold out, and null is a bucket we never successfully sampled. A client that coerces null to 0 will report GPU.ai's own polling outages as supplier stockouts, and must not interpolate across a null. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_ts** | **datetime** | Start of the bucket, UTC, aligned to the bucket width. | 
**price_per_gpu_hour** | **float** | GPU.ai&#39;s floor per-GPU hourly rate for this bucket, or null if we did not sample this bucket. Null is NOT zero. | 
**available_count** | **int** | Obtainable units across every matching offer in this bucket. 0 means we sampled and the market was sold out; null means we did not sample this bucket. | 
**node_price_per_hour** | **float** | Whole-node hourly price the per-GPU rate was divided out of. Present only when the bucket&#39;s floor came from a multi-GPU node; absent for single-GPU capacity. | [optional] 
**gpu_count** | **int** | GPUs in that node. Present only alongside &#x60;node_price_per_hour&#x60;, and it is what lets a renderer qualify a derived rate as \&quot;(from an 8-GPU node)\&quot; rather than implying single-GPU rentability. | [optional] 

## Example

```python
from gpuai_sdk.models.market_history_point import MarketHistoryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of MarketHistoryPoint from a JSON string
market_history_point_instance = MarketHistoryPoint.from_json(json)
# print the JSON string representation of the object
print(MarketHistoryPoint.to_json())

# convert the object into a dict
market_history_point_dict = market_history_point_instance.to_dict()
# create an instance of MarketHistoryPoint from a dict
market_history_point_from_dict = MarketHistoryPoint.from_dict(market_history_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


