# swagger_client.SafetyApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**safety_arrowboard_id_get**](SafetyApi.md#safety_arrowboard_id_get) | **GET** /safety/arrowboard/{id} | Return the current location and text on the arrow board
[**safety_arrowboard_id_patch**](SafetyApi.md#safety_arrowboard_id_patch) | **PATCH** /safety/arrowboard/{id} | Update the pattern on an arrow board
[**safety_arrowboards_get**](SafetyApi.md#safety_arrowboards_get) | **GET** /safety/arrowboards | Return a list of arrowboard objects
[**safety_get**](SafetyApi.md#safety_get) | **GET** /safety | Return a list of all safety equipment
[**safety_messageboard_id_get**](SafetyApi.md#safety_messageboard_id_get) | **GET** /safety/messageboard/{id} | Return the current location and text on the message board
[**safety_messageboard_id_patch**](SafetyApi.md#safety_messageboard_id_patch) | **PATCH** /safety/messageboard/{id} | Update the content on a message board
[**safety_messageboards_get**](SafetyApi.md#safety_messageboards_get) | **GET** /safety/messageboards | Return a list of messageboard objects

# **safety_arrowboard_id_get**
> ArrowBoard safety_arrowboard_id_get(id)

Return the current location and text on the arrow board

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
api_instance = swagger_client.SafetyApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for the arrowboard

try:
    # Return the current location and text on the arrow board
    api_response = api_instance.safety_arrowboard_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->safety_arrowboard_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for the arrowboard | 

### Return type

[**ArrowBoard**](ArrowBoard.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **safety_arrowboard_id_patch**
> InlineResponse2002 safety_arrowboard_id_patch(id, body=body)

Update the pattern on an arrow board

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
api_instance = swagger_client.SafetyApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for the arrowboard
body = swagger_client.Body21() # Body21 |  (optional)

try:
    # Update the pattern on an arrow board
    api_response = api_instance.safety_arrowboard_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->safety_arrowboard_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for the arrowboard | 
 **body** | [**Body21**](Body21.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **safety_arrowboards_get**
> InlineResponse20041 safety_arrowboards_get()

Return a list of arrowboard objects

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
api_instance = swagger_client.SafetyApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of arrowboard objects
    api_response = api_instance.safety_arrowboards_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->safety_arrowboards_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **safety_get**
> InlineResponse20039 safety_get()

Return a list of all safety equipment

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
api_instance = swagger_client.SafetyApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of all safety equipment
    api_response = api_instance.safety_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->safety_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **safety_messageboard_id_get**
> MessageBoard safety_messageboard_id_get(id)

Return the current location and text on the message board

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
api_instance = swagger_client.SafetyApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for the messageboard

try:
    # Return the current location and text on the message board
    api_response = api_instance.safety_messageboard_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->safety_messageboard_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for the messageboard | 

### Return type

[**MessageBoard**](MessageBoard.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **safety_messageboard_id_patch**
> InlineResponse2002 safety_messageboard_id_patch(id, body=body)

Update the content on a message board

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
api_instance = swagger_client.SafetyApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A unique identifier for the messageboard
body = swagger_client.Body20() # Body20 |  (optional)

try:
    # Update the content on a message board
    api_response = api_instance.safety_messageboard_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->safety_messageboard_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique identifier for the messageboard | 
 **body** | [**Body20**](Body20.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **safety_messageboards_get**
> InlineResponse20040 safety_messageboards_get()

Return a list of messageboard objects

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
api_instance = swagger_client.SafetyApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of messageboard objects
    api_response = api_instance.safety_messageboards_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SafetyApi->safety_messageboards_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

