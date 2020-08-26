# Crosswalk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An ID number identifying this crosswalk | 
**uri** | **str** | The URI which can be used to access this crosswalk directly | [optional] 
**name** | **str** | A text based description of this crosswalk | [optional] 
**url** | **str** | A url with more information about this specific crosswalk | [optional] 
**longitude** | **float** | The longitude of the centroid of the crosswalk | [optional] 
**latitude** | **float** | The latitude of the centroid of the crosswalk | [optional] 
**instrument** | **str** | The painted line pattern for this crosswalk | [optional] 
**refuge** | **bool** | Does the crosswalk have a central island pedestrian refuge | [optional] 
**beacon** | **str** | The beacon type used for this crosswalk | [optional] 
**phases** | **list[str]** | A list of valid phases for the crosswalk if equipped with a graphical display | [optional] 
**countdown** | **bool** | Does the crosswalk feature an instrumented phase timer | [optional] 
**audible** | **bool** | Is the crosswalk equipped with an audible warning for the crossing/countdown | [optional] 
**visor** | **str** | The type of visor installed on the beacon | [optional] 
**call_button** | **bool** | Can a pedestrian place a call or trigger this crosswalk with a button | [optional] 
**tactile_surface** | **bool** | Does the entrance to the crosswalk feature a tactile surface | [optional] 
**state** | [**CrosswalkState**](CrosswalkState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

