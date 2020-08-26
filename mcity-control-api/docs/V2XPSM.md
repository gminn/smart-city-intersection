# V2XPSM

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Static identifier if available, else temporary identifier provided by Personal Safety Device. | [optional] 
**message_set** | **str** | The original format this message was broadcast in before decoding. | [optional] 
**updated** | **datetime** | The date time this message was sent via OCTANE. | [optional] 
**longitude** | **float** | Longitude of the transmitting V2X device. | [optional] 
**latitude** | **float** | Latitude of the transmitting V2X device. | [optional] 
**elevation** | **float** | Elevation of transmitting V2X device. Units in meters | [optional] 
**speed** | **float** | Reported Velocity of V2X Device. Units in m/s | [optional] 
**heading** | **float** | 0 to 359.9875 degrees. | [optional] 
**type** | **str** | The personal safety message user type | [optional] 
**size** | **str** | Estimated size of the PSM. Large is &gt; 1.5m | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

