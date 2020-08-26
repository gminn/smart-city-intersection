# V2XSPaT

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier given for the intersection this message is related to. | [optional] 
**message_set** | **str** | The original format this message was broadcast in before decoding. | [optional] 
**updated** | **datetime** | The date time of this message was parsed. | [optional] 
**time_system** | **str** | System reported time represented as seconds.milliseconds | [optional] 
**green** | **str** | Phases which are Green. A bit string representing a true or false value for each of the 16 phases in descending order Ex. 0000000000100001 (Phase 1+6) | [optional] 
**yellow** | **str** | Phases which are Yellow. A bit string representing a true or false value for each of the 16 phases in descending order Ex. 0000000000100001 (Phase 1+6) | [optional] 
**red** | **str** | Phases which are Red. A bit string representing a true or false value for each of the 16 phases in descending order Ex. 0000000000100001 (Phase 1+6) | [optional] 
**pedestrian_clear** | **str** | Pedestrian clear state active/inactive by phase. A bit string representing a true or false value for each of the 16 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**walk_dont** | **str** | Don&#x27;t walk activity by phase. A bit string representing a true or false value for each of the 16 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**walk** | **str** | Walk activity by phase. A bit string representing a true or false value for each of the 16 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**flash** | **str** | Flashing indicator by phase. A bit string representing a true or false value for each of the 16 phases in descending order Ex. 00100001 (Phase 1+6) | [optional] 
**phases** | [**list[V2XSPaTPhases]**](V2XSPaTPhases.md) | Information about each Phase | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

