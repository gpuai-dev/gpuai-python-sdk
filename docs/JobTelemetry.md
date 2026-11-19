# JobTelemetry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peak_memory_mb** | **int** |  | 
**reservation_mb** | **int** |  | 
**gpu_memory_total_mb** | **int** |  | 
**points** | [**List[JobTelemetryPoint]**](JobTelemetryPoint.md) |  | 

## Example

```python
from gpuai_sdk.models.job_telemetry import JobTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of JobTelemetry from a JSON string
job_telemetry_instance = JobTelemetry.from_json(json)
# print the JSON string representation of the object
print(JobTelemetry.to_json())

# convert the object into a dict
job_telemetry_dict = job_telemetry_instance.to_dict()
# create an instance of JobTelemetry from a dict
job_telemetry_from_dict = JobTelemetry.from_dict(job_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


