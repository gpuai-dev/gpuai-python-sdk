# MarketHistoryResponse

A price/stock series for one (gpu_model, region, capacity_class) key.  Points cover the FULL bucket grid across the requested window, including the buckets we did not sample — a gap therefore has visible width rather than disappearing between two adjacent points. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_model** | **str** |  | 
**region** | **str** | Echoes the request. Empty means the series is MERGED across every region, the same thing it meant on the way in. | 
**capacity_class** | **str** | Echoes the request. Empty means the series is merged across both classes. | 
**cluster_size** | **int** | Echoes the request. 0 means the series is MERGED across every node shape, the same thing an omitted parameter meant on the way in. | 
**available_cluster_sizes** | **List[int]** | The node shapes that actually have rows in this window, for this gpu_model / region / capacity_class — what a size picker may honestly offer.  This is what we SAMPLED, not what we may ever sell: offering a shape a model was never listed at draws an empty chart a caller reads as a stockout. An empty array means we looked and found none. It is unaffected by the cluster_size parameter, so a picker&#39;s options never depend on which option is currently selected. | 
**bucket_seconds** | **int** | Resolution the server actually answered at. Echoed because the wide views downsample at query time, so a client must never assume 900. | 
**points** | [**List[MarketHistoryPoint]**](MarketHistoryPoint.md) |  | 

## Example

```python
from gpuai_sdk.models.market_history_response import MarketHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketHistoryResponse from a JSON string
market_history_response_instance = MarketHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(MarketHistoryResponse.to_json())

# convert the object into a dict
market_history_response_dict = market_history_response_instance.to_dict()
# create an instance of MarketHistoryResponse from a dict
market_history_response_from_dict = MarketHistoryResponse.from_dict(market_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


