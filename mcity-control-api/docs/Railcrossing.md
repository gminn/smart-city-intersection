# Railcrossing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An ID number identifying this crosswalk | 
**uri** | **str** | The URI which can be used to access this rail crossing directly | [optional] 
**name** | **str** | A text based description of the rail crossing | [optional] 
**url** | **str** | A url with more information about this specific rail crossing | [optional] 
**longitude** | **float** | The longitude of the centroid of the rail crossing | [optional] 
**latitude** | **float** | The latitude of the centroid of the rail crossing | [optional] 
**instrument** | **str** | The signal type of rail crossing | [optional] 
**audible** | **bool** | Is the rail crossing equipped with an audible warning | [optional] 
**gate** | **bool** | Is the rail crossing equipped with a gate | [optional] 
**beacon** | **str** | The beacon type used for this rail crossing | [optional] 
**phases** | **list[str]** | A list of supported phases | [optional] 
**state** | [**RailcrossingState**](RailcrossingState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

