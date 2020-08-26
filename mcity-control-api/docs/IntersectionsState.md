# IntersectionsState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reset** | **bool** | Request a reset of the timing on all traffic controllers. Reset is performed before other items in this request. | [optional] 
**enabled** | **bool** | Request the signal heads for this intersection be switched on or off. This does not shut off the controller. | [optional] 
**flash** | **bool** | Toggles the intersections between all way flash and a free timed mode. | [optional] 
**time_paused** | **bool** | Pause or un-pause ring time of this intersection. Causes all lights to freeze in current state when set True. | [optional] 
**time_clear_control** | **int** | Default is 0 - disabled. &gt; 0 setting causes control commands to be automatically cleared this input number of seconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

