# swagger_client.SignalsApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signal_id_get**](SignalsApi.md#signal_id_get) | **GET** /signal/{id} | Return an signal object with the specified ID.
[**signal_id_patch**](SignalsApi.md#signal_id_patch) | **PATCH** /signal/{id} | Allows control of a single signal set.
[**signals_get**](SignalsApi.md#signals_get) | **GET** /signals | Return a list of signal objects describing all instrumented signals within the facility.

# **signal_id_get**
> InlineResponse20015 signal_id_get(id)

Return an signal object with the specified ID.

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
api_instance = swagger_client.SignalsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A signal ID string.

try:
    # Return an signal object with the specified ID.
    api_response = api_instance.signal_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalsApi->signal_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A signal ID string. | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_id_patch**
> InlineResponse2002 signal_id_patch(id, body=body)

Allows control of a single signal set.

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
api_instance = swagger_client.SignalsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A signal ID string.
body = swagger_client.Body6() # Body6 |  (optional)

try:
    # Allows control of a single signal set.
    api_response = api_instance.signal_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalsApi->signal_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A signal ID string. | 
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signals_get**
> InlineResponse20014 signals_get()

Return a list of signal objects describing all instrumented signals within the facility.

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
api_instance = swagger_client.SignalsApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of signal objects describing all instrumented signals within the facility.
    api_response = api_instance.signals_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalsApi->signals_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

