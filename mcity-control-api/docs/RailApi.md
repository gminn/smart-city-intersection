# swagger_client.RailApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**railcrossing_id_get**](RailApi.md#railcrossing_id_get) | **GET** /railcrossing/{id} | Return an rail crossing object with the specified ID.
[**railcrossing_id_patch**](RailApi.md#railcrossing_id_patch) | **PATCH** /railcrossing/{id} | Updates an existing rail crossing status, allowing for triggering. Returns request ID on success.
[**railcrossings_get**](RailApi.md#railcrossings_get) | **GET** /railcrossings | Return a list of rail crossing objects describing all instrumented crossings within the facility.

# **railcrossing_id_get**
> InlineResponse20018 railcrossing_id_get(id)

Return an rail crossing object with the specified ID.

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
api_instance = swagger_client.RailApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A rail crossing ID string.

try:
    # Return an rail crossing object with the specified ID.
    api_response = api_instance.railcrossing_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RailApi->railcrossing_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A rail crossing ID string. | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **railcrossing_id_patch**
> InlineResponse2002 railcrossing_id_patch(id, body=body)

Updates an existing rail crossing status, allowing for triggering. Returns request ID on success.

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
api_instance = swagger_client.RailApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A rail crossing ID string.
body = swagger_client.Body7() # Body7 |  (optional)

try:
    # Updates an existing rail crossing status, allowing for triggering. Returns request ID on success.
    api_response = api_instance.railcrossing_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RailApi->railcrossing_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A rail crossing ID string. | 
 **body** | [**Body7**](Body7.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **railcrossings_get**
> InlineResponse20017 railcrossings_get()

Return a list of rail crossing objects describing all instrumented crossings within the facility.

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
api_instance = swagger_client.RailApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of rail crossing objects describing all instrumented crossings within the facility.
    api_response = api_instance.railcrossings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RailApi->railcrossings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

