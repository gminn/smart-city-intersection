# swagger_client.IntersectionsApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**intersection_id_crosswalks_get**](IntersectionsApi.md#intersection_id_crosswalks_get) | **GET** /intersection/{id}/crosswalks | Return list of crosswalks within an intersection
[**intersection_id_get**](IntersectionsApi.md#intersection_id_get) | **GET** /intersection/{id} | Return an intersection object with the specified ID.
[**intersection_id_patch**](IntersectionsApi.md#intersection_id_patch) | **PATCH** /intersection/{id} | Allows control one to many phases within an intersection.
[**intersection_id_phases_get**](IntersectionsApi.md#intersection_id_phases_get) | **GET** /intersection/{id}/phases | Return list of phases configured for an intersection
[**intersection_id_preempt_preempt_id_patch**](IntersectionsApi.md#intersection_id_preempt_preempt_id_patch) | **PATCH** /intersection/{id}/preempt/{preempt_id} | Allows enabling/disabling preconfigured preempt at an intersection.
[**intersection_id_signals_get**](IntersectionsApi.md#intersection_id_signals_get) | **GET** /intersection/{id}/signals | Return list of traffic signal configured for an intersection
[**intersection_id_stages_get**](IntersectionsApi.md#intersection_id_stages_get) | **GET** /intersection/{id}/stages | Return list of suggested control groupings for the intersection (stages)
[**intersections_get**](IntersectionsApi.md#intersections_get) | **GET** /intersections | Return a list of intersection objects.
[**intersections_patch**](IntersectionsApi.md#intersections_patch) | **PATCH** /intersections | Sets features on all configured intersections that support a feature.

# **intersection_id_crosswalks_get**
> InlineResponse20012 intersection_id_crosswalks_get(id)

Return list of crosswalks within an intersection

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
api_instance = swagger_client.IntersectionsApi(swagger_client.ApiClient(configuration))
id = 56 # int | An intersection ID string.

try:
    # Return list of crosswalks within an intersection
    api_response = api_instance.intersection_id_crosswalks_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntersectionsApi->intersection_id_crosswalks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An intersection ID string. | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intersection_id_get**
> InlineResponse2009 intersection_id_get(id)

Return an intersection object with the specified ID.

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
api_instance = swagger_client.IntersectionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | An intersection ID string.

try:
    # Return an intersection object with the specified ID.
    api_response = api_instance.intersection_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntersectionsApi->intersection_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An intersection ID string. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intersection_id_patch**
> InlineResponse2002 intersection_id_patch(id, body=body)

Allows control one to many phases within an intersection.

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
api_instance = swagger_client.IntersectionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | An intersection ID string.
body = swagger_client.Body4() # Body4 |  (optional)

try:
    # Allows control one to many phases within an intersection.
    api_response = api_instance.intersection_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntersectionsApi->intersection_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An intersection ID string. | 
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intersection_id_phases_get**
> InlineResponse20010 intersection_id_phases_get(id)

Return list of phases configured for an intersection

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
api_instance = swagger_client.IntersectionsApi(swagger_client.ApiClient(configuration))
id = 56 # int | An intersection ID string.

try:
    # Return list of phases configured for an intersection
    api_response = api_instance.intersection_id_phases_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntersectionsApi->intersection_id_phases_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An intersection ID string. | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intersection_id_preempt_preempt_id_patch**
> InlineResponse2002 intersection_id_preempt_preempt_id_patch(id, preempt_id, body=body)

Allows enabling/disabling preconfigured preempt at an intersection.

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
api_instance = swagger_client.IntersectionsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | An intersection ID string.
preempt_id = 'preempt_id_example' # str | An intersection preempt ID.
body = swagger_client.Body5() # Body5 |  (optional)

try:
    # Allows enabling/disabling preconfigured preempt at an intersection.
    api_response = api_instance.intersection_id_preempt_preempt_id_patch(id, preempt_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntersectionsApi->intersection_id_preempt_preempt_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An intersection ID string. | 
 **preempt_id** | **str**| An intersection preempt ID. | 
 **body** | [**Body5**](Body5.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intersection_id_signals_get**
> InlineResponse20011 intersection_id_signals_get(id)

Return list of traffic signal configured for an intersection

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
api_instance = swagger_client.IntersectionsApi(swagger_client.ApiClient(configuration))
id = 56 # int | An intersection ID string.

try:
    # Return list of traffic signal configured for an intersection
    api_response = api_instance.intersection_id_signals_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntersectionsApi->intersection_id_signals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An intersection ID string. | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intersection_id_stages_get**
> list[Stage] intersection_id_stages_get(id)

Return list of suggested control groupings for the intersection (stages)

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
api_instance = swagger_client.IntersectionsApi(swagger_client.ApiClient(configuration))
id = 56 # int | An intersection ID string.

try:
    # Return list of suggested control groupings for the intersection (stages)
    api_response = api_instance.intersection_id_stages_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntersectionsApi->intersection_id_stages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An intersection ID string. | 

### Return type

[**list[Stage]**](Stage.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intersections_get**
> InlineResponse2008 intersections_get()

Return a list of intersection objects.

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
api_instance = swagger_client.IntersectionsApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of intersection objects.
    api_response = api_instance.intersections_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntersectionsApi->intersections_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intersections_patch**
> InlineResponse2005 intersections_patch(body=body)

Sets features on all configured intersections that support a feature.

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
api_instance = swagger_client.IntersectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body3() # Body3 |  (optional)

try:
    # Sets features on all configured intersections that support a feature.
    api_response = api_instance.intersections_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntersectionsApi->intersections_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

