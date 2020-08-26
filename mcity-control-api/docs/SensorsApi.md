# swagger_client.SensorsApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sensor_camera_id_get**](SensorsApi.md#sensor_camera_id_get) | **GET** /sensor/camera/{id} | Return information about a camera with the specified ID.
[**sensor_camera_id_patch**](SensorsApi.md#sensor_camera_id_patch) | **PATCH** /sensor/camera/{id} | Updates a sensor state. Returns request ID on success.
[**sensor_id_get**](SensorsApi.md#sensor_id_get) | **GET** /sensor/{id} | Return information about a sensor.
[**sensor_id_patch**](SensorsApi.md#sensor_id_patch) | **PATCH** /sensor/{id} | Updates a sensor state. Returns request ID on success.
[**sensor_lidar_id_get**](SensorsApi.md#sensor_lidar_id_get) | **GET** /sensor/lidar/{id} | Return information about a LIDAR with the specified ID.
[**sensor_lidar_id_patch**](SensorsApi.md#sensor_lidar_id_patch) | **PATCH** /sensor/lidar/{id} | Updates a sensor state. Returns request ID on success.
[**sensor_package_id_get**](SensorsApi.md#sensor_package_id_get) | **GET** /sensor/package/{id} | Return information about a grouping of sensors, known as a sensor package, with the specified ID.
[**sensor_package_id_patch**](SensorsApi.md#sensor_package_id_patch) | **PATCH** /sensor/package/{id} | Updates a sensor state. Returns request ID on success.
[**sensor_radar_id_get**](SensorsApi.md#sensor_radar_id_get) | **GET** /sensor/radar/{id} | Return information about a RADAR with the specified ID.
[**sensor_radar_id_patch**](SensorsApi.md#sensor_radar_id_patch) | **PATCH** /sensor/radar/{id} | Updates a sensor state. Returns request ID on success.
[**sensors_cameras_get**](SensorsApi.md#sensors_cameras_get) | **GET** /sensors/cameras | Return a list of cameras from this facility.
[**sensors_cameras_patch**](SensorsApi.md#sensors_cameras_patch) | **PATCH** /sensors/cameras | Updates a sensor state. Returns request ID on success.
[**sensors_get**](SensorsApi.md#sensors_get) | **GET** /sensors | Return a list of sensors at this facility.
[**sensors_lidars_get**](SensorsApi.md#sensors_lidars_get) | **GET** /sensors/lidars | Return a list of LIDAR sensors from this facility.
[**sensors_lidars_patch**](SensorsApi.md#sensors_lidars_patch) | **PATCH** /sensors/lidars | Updates a sensor state. Returns request ID on success.
[**sensors_packages_get**](SensorsApi.md#sensors_packages_get) | **GET** /sensors/packages | Return a list of sensors packages and groupings from this facility.
[**sensors_packages_patch**](SensorsApi.md#sensors_packages_patch) | **PATCH** /sensors/packages | Updates a sensor state. Returns request ID on success.
[**sensors_patch**](SensorsApi.md#sensors_patch) | **PATCH** /sensors | Updates a sensor state. Returns request ID on success.
[**sensors_radars_get**](SensorsApi.md#sensors_radars_get) | **GET** /sensors/radars | Return a list of RADAR sensors from this facility.
[**sensors_radars_patch**](SensorsApi.md#sensors_radars_patch) | **PATCH** /sensors/radars | Updates a sensor state. Returns request ID on success.

# **sensor_camera_id_get**
> InlineResponse20035 sensor_camera_id_get(id)

Return information about a camera with the specified ID.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.

try:
    # Return information about a camera with the specified ID.
    api_response = api_instance.sensor_camera_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_camera_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_camera_id_patch**
> InlineResponse2002 sensor_camera_id_patch(id, body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.
body = swagger_client.Body17() # Body17 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensor_camera_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_camera_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 
 **body** | [**Body17**](Body17.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_id_get**
> InlineResponse20033 sensor_id_get(id)

Return information about a sensor.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.

try:
    # Return information about a sensor.
    api_response = api_instance.sensor_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_id_patch**
> InlineResponse2002 sensor_id_patch(id, body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.
body = swagger_client.Body15() # Body15 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensor_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 
 **body** | [**Body15**](Body15.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_lidar_id_get**
> InlineResponse20036 sensor_lidar_id_get(id)

Return information about a LIDAR with the specified ID.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.

try:
    # Return information about a LIDAR with the specified ID.
    api_response = api_instance.sensor_lidar_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_lidar_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_lidar_id_patch**
> InlineResponse2002 sensor_lidar_id_patch(id, body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.
body = swagger_client.Body18() # Body18 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensor_lidar_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_lidar_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 
 **body** | [**Body18**](Body18.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_package_id_get**
> InlineResponse20034 sensor_package_id_get(id)

Return information about a grouping of sensors, known as a sensor package, with the specified ID.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.

try:
    # Return information about a grouping of sensors, known as a sensor package, with the specified ID.
    api_response = api_instance.sensor_package_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_package_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_package_id_patch**
> InlineResponse2002 sensor_package_id_patch(id, body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.
body = swagger_client.Body16() # Body16 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensor_package_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_package_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 
 **body** | [**Body16**](Body16.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_radar_id_get**
> InlineResponse20037 sensor_radar_id_get(id)

Return information about a RADAR with the specified ID.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.

try:
    # Return information about a RADAR with the specified ID.
    api_response = api_instance.sensor_radar_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_radar_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensor_radar_id_patch**
> InlineResponse2002 sensor_radar_id_patch(id, body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A sensor ID string.
body = swagger_client.Body19() # Body19 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensor_radar_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensor_radar_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A sensor ID string. | 
 **body** | [**Body19**](Body19.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_cameras_get**
> InlineResponse20030 sensors_cameras_get()

Return a list of cameras from this facility.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of cameras from this facility.
    api_response = api_instance.sensors_cameras_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_cameras_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_cameras_patch**
> InlineResponse2002 sensors_cameras_patch(body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body12() # Body12 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensors_cameras_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_cameras_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body12**](Body12.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_get**
> InlineResponse20028 sensors_get()

Return a list of sensors at this facility.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of sensors at this facility.
    api_response = api_instance.sensors_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_lidars_get**
> InlineResponse20031 sensors_lidars_get()

Return a list of LIDAR sensors from this facility.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of LIDAR sensors from this facility.
    api_response = api_instance.sensors_lidars_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_lidars_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_lidars_patch**
> InlineResponse2002 sensors_lidars_patch(body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body13() # Body13 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensors_lidars_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_lidars_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body13**](Body13.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_packages_get**
> InlineResponse20029 sensors_packages_get()

Return a list of sensors packages and groupings from this facility.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of sensors packages and groupings from this facility.
    api_response = api_instance.sensors_packages_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_packages_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_packages_patch**
> InlineResponse2002 sensors_packages_patch(body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body11() # Body11 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensors_packages_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_packages_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body11**](Body11.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_patch**
> InlineResponse2002 sensors_patch(body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body10() # Body10 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensors_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body10**](Body10.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_radars_get**
> InlineResponse20032 sensors_radars_get()

Return a list of RADAR sensors from this facility.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of RADAR sensors from this facility.
    api_response = api_instance.sensors_radars_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_radars_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sensors_radars_patch**
> InlineResponse2002 sensors_radars_patch(body=body)

Updates a sensor state. Returns request ID on success.

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
api_instance = swagger_client.SensorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body14() # Body14 |  (optional)

try:
    # Updates a sensor state. Returns request ID on success.
    api_response = api_instance.sensors_radars_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->sensors_radars_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body14**](Body14.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

