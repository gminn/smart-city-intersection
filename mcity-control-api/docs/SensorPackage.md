# SensorPackage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An ID number identifying this sensor package | 
**uri** | **str** | The URI which can be used to access this sensor package | [optional] 
**name** | **str** | A text based description of the sensor package | [optional] 
**url** | **str** | A url with more information about this specific sensor package | [optional] 
**longitude** | **float** | The longitude of the centroid of the sensor package | [optional] 
**latitude** | **float** | The latitude of the centroid of the sensor package | [optional] 
**type** | **str** | The sensor type | [optional] 
**manufacturer** | **str** | The sensor package manufacturer | [optional] 
**model** | **str** | The model number/name of the sensor package | [optional] 
**revision** | **str** | Sensor package revision number/edition information | [optional] 
**ip_address** | **str** | The ip address of the sensor package | [optional] 
**url_web_interface** | **str** | A URL allowing control or management of the sensor package | [optional] 
**cameras** | [**list[SensorCamera]**](SensorCamera.md) | Cameras included in this sensor package | [optional] 
**lidars** | [**list[SensorLIDAR]**](SensorLIDAR.md) | LIDARs included in this sensor package | [optional] 
**radars** | [**list[SensorRADAR]**](SensorRADAR.md) | RADARs included in this sensor package | [optional] 
**state** | [**SensorState**](SensorState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

