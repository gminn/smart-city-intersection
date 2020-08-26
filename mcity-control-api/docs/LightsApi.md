# swagger_client.LightsApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**light_id_get**](LightsApi.md#light_id_get) | **GET** /light/{id} | Return a light object with the specified ID.
[**light_id_patch**](LightsApi.md#light_id_patch) | **PATCH** /light/{id} | Allows control to a light.
[**lights_get**](LightsApi.md#lights_get) | **GET** /lights | Return a list of light objects.
[**lights_patch**](LightsApi.md#lights_patch) | **PATCH** /lights | Sets features on all configured lights that support a feature.

# **light_id_get**
> InlineResponse2006 light_id_get(id)

Return a light object with the specified ID.

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
api_instance = swagger_client.LightsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A light ID string.

try:
    # Return a light object with the specified ID.
    api_response = api_instance.light_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightsApi->light_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A light ID string. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **light_id_patch**
> InlineResponse2002 light_id_patch(id, body=body)

Allows control to a light.

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
api_instance = swagger_client.LightsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A light ID string.
body = swagger_client.Body2() # Body2 |  (optional)

try:
    # Allows control to a light.
    api_response = api_instance.light_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightsApi->light_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A light ID string. | 
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lights_get**
> InlineResponse2004 lights_get()

Return a list of light objects.

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
api_instance = swagger_client.LightsApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of light objects.
    api_response = api_instance.lights_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightsApi->lights_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lights_patch**
> InlineResponse2005 lights_patch(body=body)

Sets features on all configured lights that support a feature.

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
api_instance = swagger_client.LightsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body1() # Body1 |  (optional)

try:
    # Sets features on all configured lights that support a feature.
    api_response = api_instance.lights_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LightsApi->lights_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

