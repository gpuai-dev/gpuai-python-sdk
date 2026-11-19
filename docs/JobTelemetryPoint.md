# JobTelemetryPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ts** | **datetime** |  | 
**attempt** | **int** |  | 
**memory_mb** | **int** | The job&#39;s highest GPU memory use in the window, in MiB. | 
**gpu_memory_mb** | **int** | Memory in use on the whole GPU, all jobs included, in MiB. | 
**gpu_util_pct** | **int** | Utilization of the whole GPU, in percent. | 

## Example

```python
from gpuai_sdk.models.job_telemetry_point import JobTelemetryPoint

# TODO update the JSON string below
json = "{}"
# create an instance of JobTelemetryPoint from a JSON string
job_telemetry_point_instance = JobTelemetryPoint.from_json(json)
# print the JSON string representation of the object
print(JobTelemetryPoint.to_json())

# convert the object into a dict
job_telemetry_point_dict = job_telemetry_point_instance.to_dict()
# create an instance of JobTelemetryPoint from a dict
job_telemetry_point_from_dict = JobTelemetryPoint.from_dict(job_telemetry_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


