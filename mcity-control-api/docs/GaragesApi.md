# swagger_client.GaragesApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**garage_id_get**](GaragesApi.md#garage_id_get) | **GET** /garage/{id} | Return a garage object with the specified ID.
[**garage_id_patch**](GaragesApi.md#garage_id_patch) | **PATCH** /garage/{id} | Allows control of a garage.
[**garages_get**](GaragesApi.md#garages_get) | **GET** /garages | Return a list of garages

# **garage_id_get**
> InlineResponse2001 garage_id_get(id)

Return a garage object with the specified ID.

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
api_instance = swagger_client.GaragesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A garage ID string.

try:
    # Return a garage object with the specified ID.
    api_response = api_instance.garage_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GaragesApi->garage_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A garage ID string. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **garage_id_patch**
> InlineResponse2002 garage_id_patch(id, body=body)

Allows control of a garage.

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
api_instance = swagger_client.GaragesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A garage ID string.
body = swagger_client.Body() # Body |  (optional)

try:
    # Allows control of a garage.
    api_response = api_instance.garage_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GaragesApi->garage_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A garage ID string. | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **garages_get**
> InlineResponse200 garages_get()

Return a list of garages

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
api_instance = swagger_client.GaragesApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of garages
    api_response = api_instance.garages_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GaragesApi->garages_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

