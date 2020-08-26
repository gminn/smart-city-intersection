# swagger_client.WebSocketsChannelsApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**octane_crosswalk_get**](WebSocketsChannelsApi.md#octane_crosswalk_get) | **GET** /octane/crosswalk | Channel used for publishing crosswalk_* events.
[**octane_facility_get**](WebSocketsChannelsApi.md#octane_facility_get) | **GET** /octane/facility | Channel used for publishing facility_* events.
[**octane_garage_get**](WebSocketsChannelsApi.md#octane_garage_get) | **GET** /octane/garage | Channel used for publishing garage_* events.
[**octane_gate_get**](WebSocketsChannelsApi.md#octane_gate_get) | **GET** /octane/gate | Channel used for publishing gate_* events.
[**octane_intersection_get**](WebSocketsChannelsApi.md#octane_intersection_get) | **GET** /octane/intersection | Channel used for publishing intersection_* events.
[**octane_ipc_get**](WebSocketsChannelsApi.md#octane_ipc_get) | **GET** /octane/ipc | Channel for IPC/Timing messages. Publishes user_* events.
[**octane_light_get**](WebSocketsChannelsApi.md#octane_light_get) | **GET** /octane/light | Channel used for publishing light_* events.
[**octane_railcrossing_get**](WebSocketsChannelsApi.md#octane_railcrossing_get) | **GET** /octane/railcrossing | Channel used for publishing railcrossing_* events.
[**octane_sensor_get**](WebSocketsChannelsApi.md#octane_sensor_get) | **GET** /octane/sensor | Channel used for publishing sensor_* events.
[**octane_signal_get**](WebSocketsChannelsApi.md#octane_signal_get) | **GET** /octane/signal | Channel used for publishing intersection_* events.
[**octane_user_get**](WebSocketsChannelsApi.md#octane_user_get) | **GET** /octane/user | Channel for direct messages. Publishes user_* events.
[**octane_v2x_get**](WebSocketsChannelsApi.md#octane_v2x_get) | **GET** /octane/v2x | Channel used for publishing requests and updates from V2X devices. Provides notifications when new devices are heard from.
[**octane_v2x_obu_id_parsed_get**](WebSocketsChannelsApi.md#octane_v2x_obu_id_parsed_get) | **GET** /octane/v2x_obu_[id]_parsed | formatted version of events from a specific OBU.
[**octane_v2x_obu_id_raw_get**](WebSocketsChannelsApi.md#octane_v2x_obu_id_raw_get) | **GET** /octane/v2x_obu_[id]_raw | Channel used for publishing all raw v2x_* events from a specific OBU.
[**octane_v2x_obu_parsed_get**](WebSocketsChannelsApi.md#octane_v2x_obu_parsed_get) | **GET** /octane/v2x_obu_parsed | Channel used for publishing raw v2x_* events from all known OBUs.
[**octane_v2x_obu_raw_get**](WebSocketsChannelsApi.md#octane_v2x_obu_raw_get) | **GET** /octane/v2x_obu_raw | Channel used for publishing raw v2x_* events from all known OBUs.
[**octane_v2x_rsu_id_parsed_get**](WebSocketsChannelsApi.md#octane_v2x_rsu_id_parsed_get) | **GET** /octane/v2x_rsu_[id]_parsed | JSON formatted version of events from a specific RSU.
[**octane_v2x_rsu_id_raw_get**](WebSocketsChannelsApi.md#octane_v2x_rsu_id_raw_get) | **GET** /octane/v2x_rsu_[id]_raw | Channel used for publishing all raw v2x_* events from a specific RSU.
[**octane_v2x_rsu_parsed_get**](WebSocketsChannelsApi.md#octane_v2x_rsu_parsed_get) | **GET** /octane/v2x_rsu_parsed | Channel used for publishing raw v2x_* events from all known RSUs.
[**octane_v2x_rsu_raw_get**](WebSocketsChannelsApi.md#octane_v2x_rsu_raw_get) | **GET** /octane/v2x_rsu_raw | Channel used for publishing raw v2x_* events from all known RSUs.
[**octane_weather_get**](WebSocketsChannelsApi.md#octane_weather_get) | **GET** /octane/weather | Channel used for publishing weather_* events.

# **octane_crosswalk_get**
> octane_crosswalk_get()

Channel used for publishing crosswalk_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing crosswalk_* events.
    api_instance.octane_crosswalk_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_crosswalk_get: %s\n" % e)
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

# **octane_facility_get**
> octane_facility_get()

Channel used for publishing facility_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing facility_* events.
    api_instance.octane_facility_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_facility_get: %s\n" % e)
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

# **octane_garage_get**
> octane_garage_get()

Channel used for publishing garage_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing garage_* events.
    api_instance.octane_garage_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_garage_get: %s\n" % e)
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

# **octane_gate_get**
> octane_gate_get()

Channel used for publishing gate_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing gate_* events.
    api_instance.octane_gate_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_gate_get: %s\n" % e)
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

# **octane_intersection_get**
> octane_intersection_get()

Channel used for publishing intersection_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing intersection_* events.
    api_instance.octane_intersection_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_intersection_get: %s\n" % e)
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

# **octane_ipc_get**
> octane_ipc_get()

Channel for IPC/Timing messages. Publishes user_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel for IPC/Timing messages. Publishes user_* events.
    api_instance.octane_ipc_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_ipc_get: %s\n" % e)
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

# **octane_light_get**
> octane_light_get()

Channel used for publishing light_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing light_* events.
    api_instance.octane_light_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_light_get: %s\n" % e)
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

# **octane_railcrossing_get**
> octane_railcrossing_get()

Channel used for publishing railcrossing_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing railcrossing_* events.
    api_instance.octane_railcrossing_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_railcrossing_get: %s\n" % e)
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

# **octane_sensor_get**
> octane_sensor_get()

Channel used for publishing sensor_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing sensor_* events.
    api_instance.octane_sensor_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_sensor_get: %s\n" % e)
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

# **octane_signal_get**
> octane_signal_get()

Channel used for publishing intersection_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing intersection_* events.
    api_instance.octane_signal_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_signal_get: %s\n" % e)
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

# **octane_user_get**
> octane_user_get()

Channel for direct messages. Publishes user_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel for direct messages. Publishes user_* events.
    api_instance.octane_user_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_user_get: %s\n" % e)
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

# **octane_v2x_get**
> octane_v2x_get()

Channel used for publishing requests and updates from V2X devices. Provides notifications when new devices are heard from.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing requests and updates from V2X devices. Provides notifications when new devices are heard from.
    api_instance.octane_v2x_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_v2x_get: %s\n" % e)
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

# **octane_v2x_obu_id_parsed_get**
> octane_v2x_obu_id_parsed_get()

formatted version of events from a specific OBU.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # formatted version of events from a specific OBU.
    api_instance.octane_v2x_obu_id_parsed_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_v2x_obu_id_parsed_get: %s\n" % e)
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

# **octane_v2x_obu_id_raw_get**
> octane_v2x_obu_id_raw_get()

Channel used for publishing all raw v2x_* events from a specific OBU.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing all raw v2x_* events from a specific OBU.
    api_instance.octane_v2x_obu_id_raw_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_v2x_obu_id_raw_get: %s\n" % e)
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

# **octane_v2x_obu_parsed_get**
> octane_v2x_obu_parsed_get()

Channel used for publishing raw v2x_* events from all known OBUs.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing raw v2x_* events from all known OBUs.
    api_instance.octane_v2x_obu_parsed_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_v2x_obu_parsed_get: %s\n" % e)
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

# **octane_v2x_obu_raw_get**
> octane_v2x_obu_raw_get()

Channel used for publishing raw v2x_* events from all known OBUs.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing raw v2x_* events from all known OBUs.
    api_instance.octane_v2x_obu_raw_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_v2x_obu_raw_get: %s\n" % e)
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

# **octane_v2x_rsu_id_parsed_get**
> octane_v2x_rsu_id_parsed_get()

JSON formatted version of events from a specific RSU.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # JSON formatted version of events from a specific RSU.
    api_instance.octane_v2x_rsu_id_parsed_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_v2x_rsu_id_parsed_get: %s\n" % e)
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

# **octane_v2x_rsu_id_raw_get**
> octane_v2x_rsu_id_raw_get()

Channel used for publishing all raw v2x_* events from a specific RSU.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing all raw v2x_* events from a specific RSU.
    api_instance.octane_v2x_rsu_id_raw_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_v2x_rsu_id_raw_get: %s\n" % e)
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

# **octane_v2x_rsu_parsed_get**
> octane_v2x_rsu_parsed_get()

Channel used for publishing raw v2x_* events from all known RSUs.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing raw v2x_* events from all known RSUs.
    api_instance.octane_v2x_rsu_parsed_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_v2x_rsu_parsed_get: %s\n" % e)
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

# **octane_v2x_rsu_raw_get**
> octane_v2x_rsu_raw_get()

Channel used for publishing raw v2x_* events from all known RSUs.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing raw v2x_* events from all known RSUs.
    api_instance.octane_v2x_rsu_raw_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_v2x_rsu_raw_get: %s\n" % e)
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

# **octane_weather_get**
> octane_weather_get()

Channel used for publishing weather_* events.

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
api_instance = swagger_client.WebSocketsChannelsApi(swagger_client.ApiClient(configuration))

try:
    # Channel used for publishing weather_* events.
    api_instance.octane_weather_get()
except ApiException as e:
    print("Exception when calling WebSocketsChannelsApi->octane_weather_get: %s\n" % e)
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

