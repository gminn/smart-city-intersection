# swagger_client.GatesApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gate_id_get**](GatesApi.md#gate_id_get) | **GET** /gate/{id} | Return a gate object with the specified ID.
[**gate_id_patch**](GatesApi.md#gate_id_patch) | **PATCH** /gate/{id} | Updates an existing gate status, allowing for triggering. Returns request ID on success.
[**gates_get**](GatesApi.md#gates_get) | **GET** /gates | Return a list of gate objects describing all instrumented gates within the facility.

# **gate_id_get**
> InlineResponse20024 gate_id_get(id)

Return a gate object with the specified ID.

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
api_instance = swagger_client.GatesApi(swagger_client.ApiClient(configuration))
id = 56 # int | A gate ID number.

try:
    # Return a gate object with the specified ID.
    api_response = api_instance.gate_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatesApi->gate_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A gate ID number. | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gate_id_patch**
> InlineResponse2002 gate_id_patch(id, body=body)

Updates an existing gate status, allowing for triggering. Returns request ID on success.

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
api_instance = swagger_client.GatesApi(swagger_client.ApiClient(configuration))
id = 56 # int | A gate ID number.
body = swagger_client.Body9() # Body9 |  (optional)

try:
    # Updates an existing gate status, allowing for triggering. Returns request ID on success.
    api_response = api_instance.gate_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatesApi->gate_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A gate ID number. | 
 **body** | [**Body9**](Body9.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gates_get**
> InlineResponse20023 gates_get()

Return a list of gate objects describing all instrumented gates within the facility.

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
api_instance = swagger_client.GatesApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of gate objects describing all instrumented gates within the facility.
    api_response = api_instance.gates_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatesApi->gates_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

