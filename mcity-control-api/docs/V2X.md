# V2X

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An ID number identifying this V2X device | 
**uri** | **str** | The URI which can be used to access this V2X device directly | [optional] 
**name** | **str** | A text based description of this V2X device | [optional] 
**url** | **str** | A url with more information about this specific V2X device | [optional] 
**longitude** | **float** | The longitude of the centroid of the V2X device, if fixed. | [optional] 
**latitude** | **float** | The latitude of the centroid of the V2X device, if fixed. | [optional] 
**type** | **str** |  | [optional] 
**radios_supported** | [**list[V2XRadiosSupported]**](V2XRadiosSupported.md) | A list of supported configurations for this device. | [optional] 
**manufacturer** | **str** | The OBU/RSU manufacturer | [optional] 
**model** | **str** | The OBU/RSU model | [optional] 
**revision** | **str** | Revision of the OBU/RSU | [optional] 
**vehicle_manufacturer** | **str** | Manufacturer of vehicle | [optional] 
**vehicle_model** | **str** | Model of vehicle | [optional] 
**vehicle_year** | **str** | Release year of Vehicle. | [optional] 
**state** | [**V2XState**](V2XState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

