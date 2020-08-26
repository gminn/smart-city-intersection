# swagger_client.MaintenanceApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maintenance_get**](MaintenanceApi.md#maintenance_get) | **GET** /maintenance | Return a list of all maintenance equipment
[**maintenance_lawnmower_id_get**](MaintenanceApi.md#maintenance_lawnmower_id_get) | **GET** /maintenance/lawnmower/{id} | Return the current location and state of the lawnmower
[**maintenance_lawnmower_id_patch**](MaintenanceApi.md#maintenance_lawnmower_id_patch) | **PATCH** /maintenance/lawnmower/{id} | Change the state of a lawnmower
[**maintenance_lawnmowers_get**](MaintenanceApi.md#maintenance_lawnmowers_get) | **GET** /maintenance/lawnmowers | Return a list of lawnmower objects

# **maintenance_get**
> InlineResponse20042 maintenance_get()

Return a list of all maintenance equipment

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
api_instance = swagger_client.MaintenanceApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of all maintenance equipment
    api_response = api_instance.maintenance_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_lawnmower_id_get**
> LawnMower maintenance_lawnmower_id_get(id)

Return the current location and state of the lawnmower

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
api_instance = swagger_client.MaintenanceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for the lawnmower

try:
    # Return the current location and state of the lawnmower
    api_response = api_instance.maintenance_lawnmower_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_lawnmower_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for the lawnmower | 

### Return type

[**LawnMower**](LawnMower.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_lawnmower_id_patch**
> InlineResponse2002 maintenance_lawnmower_id_patch(id, body=body)

Change the state of a lawnmower

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
api_instance = swagger_client.MaintenanceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for the lawnmower
body = swagger_client.Body22() # Body22 |  (optional)

try:
    # Change the state of a lawnmower
    api_response = api_instance.maintenance_lawnmower_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_lawnmower_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for the lawnmower | 
 **body** | [**Body22**](Body22.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_lawnmowers_get**
> InlineResponse20043 maintenance_lawnmowers_get()

Return a list of lawnmower objects

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
api_instance = swagger_client.MaintenanceApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of lawnmower objects
    api_response = api_instance.maintenance_lawnmowers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceApi->maintenance_lawnmowers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

