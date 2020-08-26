# IntersectionState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated** | **datetime** | The last time the status of this Intersection was updated | [optional] 
**enabled** | **bool** | True / False representing lit state of signal heads in intersection. | [optional] 
**time_paused** | **bool** | Is the countdown timer between phase changes for this intersection paused? | [optional] 
**time_clear_control** | **int** | Time in seconds between a control requests and when the traffic controller automatically clears that request. NTCIP 1202 Backup time. Setting to 0 disables automatic clearing of controls requests at this intersection. | [optional] 
**flash** | **bool** | Boolean value representing if the intersection is in flash (night flash) mode. | [optional] 
**call_vehicle** | **str** | Active Vehicles calls placed on each phase. A bit string representing a true or false value for each of the 8 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**call_pedestrian** | **str** | Active Pedestrian calls placed on each phase. A bit string representing a true or false value for each of the 8 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**omit** | **str** | Active Phase omits. A bit string representing a true or false value for each of the 8 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**hold** | **str** | Active Green holds by Phase. A bit string representing a true or false value for each of the 8 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**force_off** | **str** | Active force off to red requests by Phase. A bit string representing a true or false value for each of the 8 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**pedestrian_clear** | **str** | Pedestrian clear state active/inactive by phase. A bit string representing a true or false value for each of the 8 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**walk_dont** | **str** | Don&#x27;t walk activity by phase. A bit string representing a true or false value for each of the 8 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**walk** | **str** | Walk activity by phase. A bit string representing a true or false value for each of the 8 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**phases** | [**list[IntersectionStatePhases]**](IntersectionStatePhases.md) | Status for each phase at time of last update | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

