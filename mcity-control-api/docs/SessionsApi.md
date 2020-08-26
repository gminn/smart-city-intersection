# swagger_client.SessionsApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**session_get**](SessionsApi.md#session_get) | **GET** /session | Current session information.
[**session_post**](SessionsApi.md#session_post) | **POST** /session | TOKEN TYPE: SCHEDULING. Creates a new USER type token with API access between a specific date and time.
[**sessions_get**](SessionsApi.md#sessions_get) | **GET** /sessions | TOKEN TYPE: ADMIN. Lists all active sessions across all facilities.

# **session_get**
> InlineResponse20058 session_get()

Current session information.

Information about the current requesting user session.

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
api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(configuration))

try:
    # Current session information.
    api_response = api_instance.session_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->session_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_post**
> InlineResponse20059 session_post(body=body)

TOKEN TYPE: SCHEDULING. Creates a new USER type token with API access between a specific date and time.

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
api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body36() # Body36 | Request for a new token to be created. Dates are in format of 2019-03-16T16:47:04.123-04:00 (optional)

try:
    # TOKEN TYPE: SCHEDULING. Creates a new USER type token with API access between a specific date and time.
    api_response = api_instance.session_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->session_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body36**](Body36.md)| Request for a new token to be created. Dates are in format of 2019-03-16T16:47:04.123-04:00 | [optional] 

### Return type

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_get**
> InlineResponse20057 sessions_get()

TOKEN TYPE: ADMIN. Lists all active sessions across all facilities.

Lists sessions and their users. A list of currently active, valid, and non-expired sessions.

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
api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(configuration))

try:
    # TOKEN TYPE: ADMIN. Lists all active sessions across all facilities.
    api_response = api_instance.sessions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->sessions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

