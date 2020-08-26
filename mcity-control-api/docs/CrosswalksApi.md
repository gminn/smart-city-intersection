# swagger_client.CrosswalksApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crosswalk_id_get**](CrosswalksApi.md#crosswalk_id_get) | **GET** /crosswalk/{id} | Return a crosswalk object with the specified ID.
[**crosswalk_id_patch**](CrosswalksApi.md#crosswalk_id_patch) | **PATCH** /crosswalk/{id} | Updates an existing crosswalk status, allowing for triggering. Returns request ID on success.
[**crosswalks_get**](CrosswalksApi.md#crosswalks_get) | **GET** /crosswalks | Return a list of crosswalk objects describing all instrumented crossings within the facility.

# **crosswalk_id_get**
> InlineResponse20021 crosswalk_id_get(id)

Return a crosswalk object with the specified ID.

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
api_instance = swagger_client.CrosswalksApi(swagger_client.ApiClient(configuration))
id = 56 # int | A crosswalk ID number.

try:
    # Return a crosswalk object with the specified ID.
    api_response = api_instance.crosswalk_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrosswalksApi->crosswalk_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A crosswalk ID number. | 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crosswalk_id_patch**
> InlineResponse2002 crosswalk_id_patch(id, body=body)

Updates an existing crosswalk status, allowing for triggering. Returns request ID on success.

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
api_instance = swagger_client.CrosswalksApi(swagger_client.ApiClient(configuration))
id = 56 # int | A crosswalk ID number.
body = swagger_client.Body8() # Body8 |  (optional)

try:
    # Updates an existing crosswalk status, allowing for triggering. Returns request ID on success.
    api_response = api_instance.crosswalk_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrosswalksApi->crosswalk_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A crosswalk ID number. | 
 **body** | [**Body8**](Body8.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crosswalks_get**
> InlineResponse20020 crosswalks_get()

Return a list of crosswalk objects describing all instrumented crossings within the facility.

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
api_instance = swagger_client.CrosswalksApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of crosswalk objects describing all instrumented crossings within the facility.
    api_response = api_instance.crosswalks_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CrosswalksApi->crosswalks_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

