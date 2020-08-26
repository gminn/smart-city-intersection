# Intersection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An ID number identifying this intersection | 
**uri** | **str** | The URI which can be used to access this signal set directly | [optional] 
**name** | **str** | A text based description of the signal | [optional] 
**url** | **str** | A url with more information about this specific intersection | [optional] 
**longitude** | **float** | The longitude of the centroid of the signal set | [optional] 
**latitude** | **float** | The latitude of the centroid of the signal set | [optional] 
**instrument** | **str** | The intersection instrument type | [optional] 
**phases** | [**list[Phase]**](Phase.md) | A listing of configured non-conflicting sets of phases that can be used for control. | [optional] 
**stages** | [**list[IntersectionStages]**](IntersectionStages.md) | A listing of configured non-conflicting sets of phases that can be used for control. | [optional] 
**style** | **str** | Describes the number of road segments entering the intersection | [optional] 
**street_main** | **str** | The name of the street which is considered to be the main street by the traffic controller | [optional] 
**street_cross** | **str** | The name of the second street which is considered the cross street by the traffic controller | [optional] 
**v2x_intersection_id** | **str** | Identifier for this intersection used in V2X messages such as MAP and SPaT. | [optional] 
**state** | [**IntersectionState**](IntersectionState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

