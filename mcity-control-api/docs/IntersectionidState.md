# IntersectionidState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Turn signal heads at this intersection on or off. | [optional] 
**omit** | **str** | Omit specified phases. A bit string representing request for all 8 phases in descending order. | [optional] 
**hold** | **str** | Hold specified phases green. A bit string representing request for all 8 phases in descending order. | [optional] 
**force_off** | **str** | Force off specified phases. A bit string representing request for all 8 phases in descending order. | [optional] 
**omit_pedestrian** | **str** | Omit pedestrian call for specified phases. A bit string representing 8 phases in descending order. | [optional] 
**call_vehicle** | **str** | A vehicle call will be placed on specified phases. A bit string representing 8 phases in descending order. | [optional] 
**call_pedestrian** | **str** | A pedestrian call will be placed on specified phases. 8 phases in descending order. | [optional] 
**reset** | **bool** | Request a reset of the timing on this traffic controller. Reset is performed before other items in this request. | [optional] 
**flash** | **bool** | Toggles the intersection between an all way flash and a free timed mode. | [optional] 
**time_paused** | **bool** | Pause or un-pause ring time of this intersection. Causes all lights to freeze in current state. | [optional] 
**time_clear_control** | **int** | Default is 0 - disabled. Changing this per traffic controller causes control commands to be cleared after input number of seconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

