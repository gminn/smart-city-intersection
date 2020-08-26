# swagger_client.FacilityApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facilities_get**](FacilityApi.md#facilities_get) | **GET** /facilities | Return information about facilities managed by this OCTANE instance.
[**facility_chat_post**](FacilityApi.md#facility_chat_post) | **POST** /facility/chat | Post a message to the facility chat through ReST.
[**facility_get**](FacilityApi.md#facility_get) | **GET** /facility | Return information about the primary reservation facility and current reservation.
[**facility_notification_post**](FacilityApi.md#facility_notification_post) | **POST** /facility/notification | TOKEN TYPE: ADMIN. Post a message to the facility notification system.

# **facilities_get**
> InlineResponse20044 facilities_get()

Return information about facilities managed by this OCTANE instance.

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
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))

try:
    # Return information about facilities managed by this OCTANE instance.
    api_response = api_instance.facilities_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->facilities_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facility_chat_post**
> InlineResponse20045 facility_chat_post(body=body)

Post a message to the facility chat through ReST.

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
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body23() # Body23 |  (optional)

try:
    # Post a message to the facility chat through ReST.
    api_response = api_instance.facility_chat_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->facility_chat_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body23**](Body23.md)|  | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facility_get**
> Facility facility_get()

Return information about the primary reservation facility and current reservation.

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
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))

try:
    # Return information about the primary reservation facility and current reservation.
    api_response = api_instance.facility_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->facility_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Facility**](Facility.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facility_notification_post**
> InlineResponse20046 facility_notification_post(body=body)

TOKEN TYPE: ADMIN. Post a message to the facility notification system.

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
api_instance = swagger_client.FacilityApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body24() # Body24 |  (optional)

try:
    # TOKEN TYPE: ADMIN. Post a message to the facility notification system.
    api_response = api_instance.facility_notification_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacilityApi->facility_notification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body24**](Body24.md)|  | [optional] 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

