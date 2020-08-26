# V2XBSM

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Static identifier if available, else temporary identifier provided by OBU. | [optional] 
**id_temporary** | **str** | Temporary identifier | [optional] 
**id_fixed** | **str** | Permanent vehicle identifier for known vehicles. | [optional] 
**message_set** | **str** | The original format this message was broadcast in before decoding. | [optional] 
**vehicle_length** | **float** | Vehicle length in Meters | [optional] 
**vehicle_width** | **float** | Vehicle width in Meters | [optional] 
**updated** | **datetime** | The date time this message was sent via OCTANE. | [optional] 
**longitude** | **float** | Longitude of the transmitting V2X device. | [optional] 
**latitude** | **float** | Latitude of the transmitting V2X device. | [optional] 
**elevation** | **float** | Elevation of transmitting V2X device. Units in meters | [optional] 
**speed** | **float** | Reported Velocity of V2X Device. Units in meters/second | [optional] 
**heading** | **float** | 0 to 359.9875 degrees. | [optional] 
**angle** | **float** | 0 to 359.9875 degrees. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

