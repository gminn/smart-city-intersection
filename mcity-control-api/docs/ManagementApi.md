# swagger_client.ManagementApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**management_device_callback_post**](ManagementApi.md#management_device_callback_post) | **POST** /management/device/callback | TOKEN TYPE: DEVICE. Handles callbacks from physical devices connected to API.
[**management_facility_reset_post**](ManagementApi.md#management_facility_reset_post) | **POST** /management/facility/reset | TOKEN TYPE: USER. Reset controllable items within the facility.
[**management_favorite_module_name_favorite_id_delete**](ManagementApi.md#management_favorite_module_name_favorite_id_delete) | **DELETE** /management/favorite/{moduleName}/{favoriteId} | Delete a favorite from the database.
[**management_favorite_post**](ManagementApi.md#management_favorite_post) | **POST** /management/favorite | Add a favorite to database.
[**management_favorites_get**](ManagementApi.md#management_favorites_get) | **GET** /management/favorites | Retrieve list of all favorites.
[**management_modules_get**](ManagementApi.md#management_modules_get) | **GET** /management/modules | Return a list of Modules supported by this instance of Octane
[**management_polling_intersections_patch**](ManagementApi.md#management_polling_intersections_patch) | **PATCH** /management/polling/intersections | TOKEN TYPE: ADMIN. Start/Stop Intersection Traffic signal polling.

# **management_device_callback_post**
> InlineResponse2002 management_device_callback_post(body=body)

TOKEN TYPE: DEVICE. Handles callbacks from physical devices connected to API.

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
api_instance = swagger_client.ManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body35() # Body35 | External devices use this to modify state of API managed device state. (optional)

try:
    # TOKEN TYPE: DEVICE. Handles callbacks from physical devices connected to API.
    api_response = api_instance.management_device_callback_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementApi->management_device_callback_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body35**](Body35.md)| External devices use this to modify state of API managed device state. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **management_facility_reset_post**
> InlineResponse2002 management_facility_reset_post(body=body)

TOKEN TYPE: USER. Reset controllable items within the facility.

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
api_instance = swagger_client.ManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body34() # Body34 | Modify the state of all devices in the facility (optional)

try:
    # TOKEN TYPE: USER. Reset controllable items within the facility.
    api_response = api_instance.management_facility_reset_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementApi->management_facility_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body34**](Body34.md)| Modify the state of all devices in the facility | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **management_favorite_module_name_favorite_id_delete**
> InlineResponse20056 management_favorite_module_name_favorite_id_delete(module_name, favorite_id)

Delete a favorite from the database.

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
api_instance = swagger_client.ManagementApi(swagger_client.ApiClient(configuration))
module_name = 'module_name_example' # str | Type of infrastructure
favorite_id = 56 # int | Type of infrastructure id

try:
    # Delete a favorite from the database.
    api_response = api_instance.management_favorite_module_name_favorite_id_delete(module_name, favorite_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementApi->management_favorite_module_name_favorite_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| Type of infrastructure | 
 **favorite_id** | **int**| Type of infrastructure id | 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **management_favorite_post**
> Favorite management_favorite_post(body=body)

Add a favorite to database.

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
api_instance = swagger_client.ManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body32() # Body32 |  (optional)

try:
    # Add a favorite to database.
    api_response = api_instance.management_favorite_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementApi->management_favorite_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body32**](Body32.md)|  | [optional] 

### Return type

[**Favorite**](Favorite.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **management_favorites_get**
> InlineResponse20055 management_favorites_get()

Retrieve list of all favorites.

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
api_instance = swagger_client.ManagementApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve list of all favorites.
    api_response = api_instance.management_favorites_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementApi->management_favorites_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **management_modules_get**
> InlineResponse20054 management_modules_get()

Return a list of Modules supported by this instance of Octane

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
api_instance = swagger_client.ManagementApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of Modules supported by this instance of Octane
    api_response = api_instance.management_modules_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementApi->management_modules_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **management_polling_intersections_patch**
> InlineResponse2002 management_polling_intersections_patch(body=body)

TOKEN TYPE: ADMIN. Start/Stop Intersection Traffic signal polling.

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
api_instance = swagger_client.ManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body33() # Body33 | Modifications to the process that controls intersection updates (optional)

try:
    # TOKEN TYPE: ADMIN. Start/Stop Intersection Traffic signal polling.
    api_response = api_instance.management_polling_intersections_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagementApi->management_polling_intersections_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body33**](Body33.md)| Modifications to the process that controls intersection updates | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

