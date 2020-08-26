# Signal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An ID number identifying this signal set | 
**uri** | **str** | The URI which can be used to access this signal set directly | [optional] 
**name** | **str** | A text based description of the signal | [optional] 
**url** | **str** | A url with more information about this specific signal | [optional] 
**longitude** | **float** | The longitude of the centroid of the signal set | [optional] 
**latitude** | **float** | The latitude of the centroid of the signal set | [optional] 
**instrument** | **str** | The signal type | [optional] 
**direction_facing** | **str** | The direction the signal head is facing | [optional] 
**direction_traffic** | **str** | The direction of traffic this signal controls. | [optional] 
**orientation** | **str** | Describes the mounting orientation of the signal heads | [optional] 
**height** | **float** | Height of signal head to road surface in facility units. | [optional] 
**pole** | **bool** | Is signal mounted to a side pole. | [optional] 
**mast** | **bool** | Is signal mounted to a mast off the pole pole. | [optional] 
**mast_angle** | **bool** | Is mast angled off the pole | [optional] 
**wire** | **bool** | Is the signal mounted by wire to the mast or pole | [optional] 
**backplate** | **bool** | Does the signal have a backplate? | [optional] 
**left** | **bool** | This signal set has a signal pointing in this direction | [optional] 
**right** | **bool** | This signal set has a signal pointing in this direction | [optional] 
**straight** | **bool** | This signal set has a signal pointing in this direction | [optional] 
**state** | [**SignalState**](SignalState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

