# swagger_client.WebSocketsEventsApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octane_auth_fail_get**](WebSocketsEventsApi.md#octane_auth_fail_get) | **GET** /octane/auth_fail | Event emitted to user if authentication through socket.io fails. User is then disconnected.
[**octane_auth_ok_get**](WebSocketsEventsApi.md#octane_auth_ok_get) | **GET** /octane/auth_ok | Event emitted on success of authentication.
[**octane_auth_post**](WebSocketsEventsApi.md#octane_auth_post) | **POST** /octane/auth | Event emitted to server when user wishes to authenticate.
[**octane_channels_get**](WebSocketsEventsApi.md#octane_channels_get) | **GET** /octane/channels | Emitted in response to request for OCTANE channels.
[**octane_channels_post**](WebSocketsEventsApi.md#octane_channels_post) | **POST** /octane/channels | Event to be submitted to request current users channels and all valid channels.
[**octane_crosswalk_request_get**](WebSocketsEventsApi.md#octane_crosswalk_request_get) | **GET** /octane/crosswalk_request | Event emitted when a request to a railcrossing is being serviced.
[**octane_crosswalk_update_get**](WebSocketsEventsApi.md#octane_crosswalk_update_get) | **GET** /octane/crosswalk_update | Event emitted on update of railcrossing state.
[**octane_facility_message_get**](WebSocketsEventsApi.md#octane_facility_message_get) | **GET** /octane/facility_message | Event emitted for scheduling notifications, staff request, or emergency.
[**octane_facility_request_get**](WebSocketsEventsApi.md#octane_facility_request_get) | **GET** /octane/facility_request | Event emitted for facility wide requests.
[**octane_facility_update_get**](WebSocketsEventsApi.md#octane_facility_update_get) | **GET** /octane/facility_update | Event emitted for facility wide status updates.
[**octane_garage_request_get**](WebSocketsEventsApi.md#octane_garage_request_get) | **GET** /octane/garage_request | Event published when request to change state was made on this garage.
[**octane_garage_update_get**](WebSocketsEventsApi.md#octane_garage_update_get) | **GET** /octane/garage_update | Event emitted when the state of a garage is updated.
[**octane_gate_request_get**](WebSocketsEventsApi.md#octane_gate_request_get) | **GET** /octane/gate_request | Event emitted when a request to a gate is being serviced.
[**octane_gate_update_get**](WebSocketsEventsApi.md#octane_gate_update_get) | **GET** /octane/gate_update | Event emitted on update of gate state.
[**octane_intersection_request_get**](WebSocketsEventsApi.md#octane_intersection_request_get) | **GET** /octane/intersection_request | Event published when request to change state was made on this intersection.
[**octane_intersection_update_get**](WebSocketsEventsApi.md#octane_intersection_update_get) | **GET** /octane/intersection_update | Event emitted when the state of an intersection is updated.
[**octane_ipc_message_get**](WebSocketsEventsApi.md#octane_ipc_message_get) | **GET** /octane/ipc_message | Event emitted to other users when a client emits an IPC message to others listening.
[**octane_join_get**](WebSocketsEventsApi.md#octane_join_get) | **GET** /octane/join | Event emitted to other users when a user joins a channel successfully.
[**octane_join_post**](WebSocketsEventsApi.md#octane_join_post) | **POST** /octane/join | Event to be submitted for user to join a specified channel.
[**octane_leave_get**](WebSocketsEventsApi.md#octane_leave_get) | **GET** /octane/leave | Event emitted to other users when a user leaves a channel successfully.
[**octane_leave_post**](WebSocketsEventsApi.md#octane_leave_post) | **POST** /octane/leave | Event to be submitted for user to leave a specified channel.
[**octane_light_request_get**](WebSocketsEventsApi.md#octane_light_request_get) | **GET** /octane/light_request | Event published when request to change state was made on this light.
[**octane_light_update_get**](WebSocketsEventsApi.md#octane_light_update_get) | **GET** /octane/light_update | Event emitted when the state of a light is updated.
[**octane_railcrossing_request_get**](WebSocketsEventsApi.md#octane_railcrossing_request_get) | **GET** /octane/railcrossing_request | Event emitted when a request to a railcrossing is being serviced.
[**octane_railcrossing_update_get**](WebSocketsEventsApi.md#octane_railcrossing_update_get) | **GET** /octane/railcrossing_update | Event emitted on update of railcrossing state.
[**octane_sensor_request_get**](WebSocketsEventsApi.md#octane_sensor_request_get) | **GET** /octane/sensor_request | Event published when request to change state was made on this sensor.
[**octane_sensor_update_get**](WebSocketsEventsApi.md#octane_sensor_update_get) | **GET** /octane/sensor_update | Event emitted when the state of a sensor is updated.
[**octane_signal_request_get**](WebSocketsEventsApi.md#octane_signal_request_get) | **GET** /octane/signal_request | Event emitted when a request to a signal is being serviced.
[**octane_signal_update_get**](WebSocketsEventsApi.md#octane_signal_update_get) | **GET** /octane/signal_update | Event emitted on update of signal state.
[**octane_user_message_get**](WebSocketsEventsApi.md#octane_user_message_get) | **GET** /octane/user_message | Event emitted to other users when a user emits in the user channel.
[**octane_user_message_post**](WebSocketsEventsApi.md#octane_user_message_post) | **POST** /octane/user_message | Event to be submitted for broadcast to the user channel only.
[**octane_v2x_bsm_get**](WebSocketsEventsApi.md#octane_v2x_bsm_get) | **GET** /octane/v2x_BSM | On receipt of a V2X BSM message, this event is emitted with a parsed version of the message.
[**octane_v2x_bsm_post**](WebSocketsEventsApi.md#octane_v2x_bsm_post) | **POST** /octane/v2x_BSM | Broadcast a V2X BSM message through an RSU
[**octane_v2x_new_get**](WebSocketsEventsApi.md#octane_v2x_new_get) | **GET** /octane/v2x_new | COMING SOON - Event emitted when a new V2X device is heard from and added to the V2X device listing.
[**octane_v2x_psm_get**](WebSocketsEventsApi.md#octane_v2x_psm_get) | **GET** /octane/v2x_PSM | On receipt of a V2X PSM message, this event is emitted with a parsed version of the message.
[**octane_v2x_psm_post**](WebSocketsEventsApi.md#octane_v2x_psm_post) | **POST** /octane/v2x_PSM | Broadcast a V2X BSM message through an RSU
[**octane_v2x_raw_get**](WebSocketsEventsApi.md#octane_v2x_raw_get) | **GET** /octane/v2x_raw | Event emitted on message between V2X devices.
[**octane_v2x_request_get**](WebSocketsEventsApi.md#octane_v2x_request_get) | **GET** /octane/v2x_request | Event emitted on request to a V2X device.
[**octane_v2x_s_pa_t_get**](WebSocketsEventsApi.md#octane_v2x_s_pa_t_get) | **GET** /octane/v2x_SPaT | On receipt of a V2X SPaT message, this event is emitted with a parsed version of the message.
[**octane_v2x_update_get**](WebSocketsEventsApi.md#octane_v2x_update_get) | **GET** /octane/v2x_update | Event emitted on update of V2X device state.
[**octane_weather_alert_get**](WebSocketsEventsApi.md#octane_weather_alert_get) | **GET** /octane/weather_alert | Event emitted to users when a new weather alert is broadcast.
[**octane_weather_alert_update_get**](WebSocketsEventsApi.md#octane_weather_alert_update_get) | **GET** /octane/weather_alert_update | Event emitted to users when a weather alert is sent to OCTANE.

# **octane_auth_fail_get**
> InlineResponse20061 octane_auth_fail_get()

Event emitted to user if authentication through socket.io fails. User is then disconnected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted to user if authentication through socket.io fails. User is then disconnected.
    api_response = api_instance.octane_auth_fail_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_auth_fail_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_auth_ok_get**
> InlineResponse20060 octane_auth_ok_get()

Event emitted on success of authentication.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted on success of authentication.
    api_response = api_instance.octane_auth_ok_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_auth_ok_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_auth_post**
> octane_auth_post(body=body)

Event emitted to server when user wishes to authenticate.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body40() # Body40 |  (optional)

try:
    # Event emitted to server when user wishes to authenticate.
    api_instance.octane_auth_post(body=body)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_auth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body40**](Body40.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_channels_get**
> list[InlineResponse20062] octane_channels_get()

Emitted in response to request for OCTANE channels.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Emitted in response to request for OCTANE channels.
    api_response = api_instance.octane_channels_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_channels_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20062]**](InlineResponse20062.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_channels_post**
> octane_channels_post()

Event to be submitted to request current users channels and all valid channels.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event to be submitted to request current users channels and all valid channels.
    api_instance.octane_channels_post()
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_channels_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_crosswalk_request_get**
> list[Crosswalk] octane_crosswalk_request_get()

Event emitted when a request to a railcrossing is being serviced.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted when a request to a railcrossing is being serviced.
    api_response = api_instance.octane_crosswalk_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_crosswalk_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Crosswalk]**](Crosswalk.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_crosswalk_update_get**
> InlineResponse20022 octane_crosswalk_update_get()

Event emitted on update of railcrossing state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted on update of railcrossing state.
    api_response = api_instance.octane_crosswalk_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_crosswalk_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_facility_message_get**
> FacilityMessage octane_facility_message_get()

Event emitted for scheduling notifications, staff request, or emergency.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted for scheduling notifications, staff request, or emergency.
    api_response = api_instance.octane_facility_message_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_facility_message_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FacilityMessage**](FacilityMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_facility_request_get**
> list[Facility] octane_facility_request_get()

Event emitted for facility wide requests.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted for facility wide requests.
    api_response = api_instance.octane_facility_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_facility_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Facility]**](Facility.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_facility_update_get**
> list[Facility] octane_facility_update_get()

Event emitted for facility wide status updates.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted for facility wide status updates.
    api_response = api_instance.octane_facility_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_facility_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Facility]**](Facility.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_garage_request_get**
> list[Garage] octane_garage_request_get()

Event published when request to change state was made on this garage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event published when request to change state was made on this garage.
    api_response = api_instance.octane_garage_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_garage_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Garage]**](Garage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_garage_update_get**
> InlineResponse2003 octane_garage_update_get()

Event emitted when the state of a garage is updated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted when the state of a garage is updated.
    api_response = api_instance.octane_garage_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_garage_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_gate_request_get**
> list[Gate] octane_gate_request_get()

Event emitted when a request to a gate is being serviced.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted when a request to a gate is being serviced.
    api_response = api_instance.octane_gate_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_gate_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Gate]**](Gate.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_gate_update_get**
> InlineResponse20025 octane_gate_update_get()

Event emitted on update of gate state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted on update of gate state.
    api_response = api_instance.octane_gate_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_gate_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_intersection_request_get**
> list[Intersection] octane_intersection_request_get()

Event published when request to change state was made on this intersection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event published when request to change state was made on this intersection.
    api_response = api_instance.octane_intersection_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_intersection_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Intersection]**](Intersection.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_intersection_update_get**
> InlineResponse20013 octane_intersection_update_get()

Event emitted when the state of an intersection is updated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted when the state of an intersection is updated.
    api_response = api_instance.octane_intersection_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_intersection_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_ipc_message_get**
> IPCMessage octane_ipc_message_get()

Event emitted to other users when a client emits an IPC message to others listening.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted to other users when a client emits an IPC message to others listening.
    api_response = api_instance.octane_ipc_message_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_ipc_message_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IPCMessage**](IPCMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_join_get**
> octane_join_get()

Event emitted to other users when a user joins a channel successfully.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted to other users when a user joins a channel successfully.
    api_instance.octane_join_get()
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_join_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_join_post**
> octane_join_post(body=body)

Event to be submitted for user to join a specified channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body38() # Body38 |  (optional)

try:
    # Event to be submitted for user to join a specified channel.
    api_instance.octane_join_post(body=body)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_join_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body38**](Body38.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_leave_get**
> octane_leave_get()

Event emitted to other users when a user leaves a channel successfully.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted to other users when a user leaves a channel successfully.
    api_instance.octane_leave_get()
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_leave_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_leave_post**
> octane_leave_post(body=body)

Event to be submitted for user to leave a specified channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body39() # Body39 |  (optional)

try:
    # Event to be submitted for user to leave a specified channel.
    api_instance.octane_leave_post(body=body)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_leave_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body39**](Body39.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_light_request_get**
> list[Light] octane_light_request_get()

Event published when request to change state was made on this light.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event published when request to change state was made on this light.
    api_response = api_instance.octane_light_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_light_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Light]**](Light.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_light_update_get**
> InlineResponse2007 octane_light_update_get()

Event emitted when the state of a light is updated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted when the state of a light is updated.
    api_response = api_instance.octane_light_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_light_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_railcrossing_request_get**
> list[Railcrossing] octane_railcrossing_request_get()

Event emitted when a request to a railcrossing is being serviced.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted when a request to a railcrossing is being serviced.
    api_response = api_instance.octane_railcrossing_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_railcrossing_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Railcrossing]**](Railcrossing.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_railcrossing_update_get**
> InlineResponse20019 octane_railcrossing_update_get()

Event emitted on update of railcrossing state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted on update of railcrossing state.
    api_response = api_instance.octane_railcrossing_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_railcrossing_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_sensor_request_get**
> list[SensorState] octane_sensor_request_get()

Event published when request to change state was made on this sensor.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event published when request to change state was made on this sensor.
    api_response = api_instance.octane_sensor_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_sensor_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SensorState]**](SensorState.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_sensor_update_get**
> InlineResponse20038 octane_sensor_update_get()

Event emitted when the state of a sensor is updated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted when the state of a sensor is updated.
    api_response = api_instance.octane_sensor_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_sensor_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_signal_request_get**
> list[Signal] octane_signal_request_get()

Event emitted when a request to a signal is being serviced.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted when a request to a signal is being serviced.
    api_response = api_instance.octane_signal_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_signal_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Signal]**](Signal.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_signal_update_get**
> InlineResponse20016 octane_signal_update_get()

Event emitted on update of signal state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted on update of signal state.
    api_response = api_instance.octane_signal_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_signal_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_user_message_get**
> UserMessage octane_user_message_get()

Event emitted to other users when a user emits in the user channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted to other users when a user emits in the user channel.
    api_response = api_instance.octane_user_message_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_user_message_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserMessage**](UserMessage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_user_message_post**
> octane_user_message_post(body=body)

Event to be submitted for broadcast to the user channel only.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body37() # Body37 |  (optional)

try:
    # Event to be submitted for broadcast to the user channel only.
    api_instance.octane_user_message_post(body=body)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_user_message_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body37**](Body37.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_v2x_bsm_get**
> V2XBSM octane_v2x_bsm_get()

On receipt of a V2X BSM message, this event is emitted with a parsed version of the message.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # On receipt of a V2X BSM message, this event is emitted with a parsed version of the message.
    api_response = api_instance.octane_v2x_bsm_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_v2x_bsm_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V2XBSM**](V2XBSM.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_v2x_bsm_post**
> octane_v2x_bsm_post(body=body)

Broadcast a V2X BSM message through an RSU

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body30() # Body30 |  (optional)

try:
    # Broadcast a V2X BSM message through an RSU
    api_instance.octane_v2x_bsm_post(body=body)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_v2x_bsm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body30**](Body30.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_v2x_new_get**
> list[V2X] octane_v2x_new_get()

COMING SOON - Event emitted when a new V2X device is heard from and added to the V2X device listing.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # COMING SOON - Event emitted when a new V2X device is heard from and added to the V2X device listing.
    api_response = api_instance.octane_v2x_new_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_v2x_new_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V2X]**](V2X.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_v2x_psm_get**
> V2XPSM octane_v2x_psm_get()

On receipt of a V2X PSM message, this event is emitted with a parsed version of the message.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # On receipt of a V2X PSM message, this event is emitted with a parsed version of the message.
    api_response = api_instance.octane_v2x_psm_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_v2x_psm_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V2XPSM**](V2XPSM.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_v2x_psm_post**
> octane_v2x_psm_post(body=body)

Broadcast a V2X BSM message through an RSU

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body31() # Body31 |  (optional)

try:
    # Broadcast a V2X BSM message through an RSU
    api_instance.octane_v2x_psm_post(body=body)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_v2x_psm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body31**](Body31.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_v2x_raw_get**
> V2XRaw octane_v2x_raw_get()

Event emitted on message between V2X devices.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted on message between V2X devices.
    api_response = api_instance.octane_v2x_raw_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_v2x_raw_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V2XRaw**](V2XRaw.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_v2x_request_get**
> list[V2X] octane_v2x_request_get()

Event emitted on request to a V2X device.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted on request to a V2X device.
    api_response = api_instance.octane_v2x_request_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_v2x_request_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V2X]**](V2X.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_v2x_s_pa_t_get**
> list[V2XSPaT] octane_v2x_s_pa_t_get()

On receipt of a V2X SPaT message, this event is emitted with a parsed version of the message.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # On receipt of a V2X SPaT message, this event is emitted with a parsed version of the message.
    api_response = api_instance.octane_v2x_s_pa_t_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_v2x_s_pa_t_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[V2XSPaT]**](V2XSPaT.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_v2x_update_get**
> InlineResponse20053 octane_v2x_update_get()

Event emitted on update of V2X device state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted on update of V2X device state.
    api_response = api_instance.octane_v2x_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_v2x_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_weather_alert_get**
> WeatherAlert octane_weather_alert_get()

Event emitted to users when a new weather alert is broadcast.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted to users when a new weather alert is broadcast.
    api_response = api_instance.octane_weather_alert_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_weather_alert_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WeatherAlert**](WeatherAlert.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **octane_weather_alert_update_get**
> InlineResponse20027 octane_weather_alert_update_get()

Event emitted to users when a weather alert is sent to OCTANE.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.WebSocketsEventsApi(swagger_client.ApiClient(configuration))

try:
    # Event emitted to users when a weather alert is sent to OCTANE.
    api_response = api_instance.octane_weather_alert_update_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebSocketsEventsApi->octane_weather_alert_update_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

