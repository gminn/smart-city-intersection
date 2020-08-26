# swagger_client.V2XApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2x_get**](V2XApi.md#v2x_get) | **GET** /v2x | Return a list of V2X devices known to OCTANE.
[**v2x_id_get**](V2XApi.md#v2x_id_get) | **GET** /v2x/{id} | Return a v2x object with the specified ID.
[**v2x_id_patch**](V2XApi.md#v2x_id_patch) | **PATCH** /v2x/{id} | Updates an existing v2x status, allowing for triggering. Returns request ID on success.
[**v2x_obu_id_get**](V2XApi.md#v2x_obu_id_get) | **GET** /v2x/obu/{id} | Return a v2x object with the specified ID.
[**v2x_obu_id_patch**](V2XApi.md#v2x_obu_id_patch) | **PATCH** /v2x/obu/{id} | Updates an existing v2x status, allowing for triggering. Returns request ID on success.
[**v2x_obus_get**](V2XApi.md#v2x_obus_get) | **GET** /v2x/obus | Return a list of V2X OBUs known to OCTANE.
[**v2x_obus_patch**](V2XApi.md#v2x_obus_patch) | **PATCH** /v2x/obus | Updates an existing and capable V2X OBUs. Returns request ID on success.
[**v2x_rsu_id_bsm_post**](V2XApi.md#v2x_rsu_id_bsm_post) | **POST** /v2x/rsu/{id}/bsm | For RSUs with support, pack posted data into active protocol format and broadcasts the BSM.  Request body type allows for sending a pre-packed message to be sent as a direct payload or for a JSON format that will be encoded to the appropriate message format and broadcast serverside. request ID on success.
[**v2x_rsu_id_bsms_post**](V2XApi.md#v2x_rsu_id_bsms_post) | **POST** /v2x/rsu/{id}/bsms | For RSUs with support, pack posted data into active protocol format and broadcasts each row through the BSM. request ID on success.
[**v2x_rsu_id_get**](V2XApi.md#v2x_rsu_id_get) | **GET** /v2x/rsu/{id} | Return a v2x object with the specified ID.
[**v2x_rsu_id_patch**](V2XApi.md#v2x_rsu_id_patch) | **PATCH** /v2x/rsu/{id} | Updates an existing v2x status, allowing for triggering. Returns request ID on success.
[**v2x_rsu_id_psm_post**](V2XApi.md#v2x_rsu_id_psm_post) | **POST** /v2x/rsu/{id}/psm | For RSUs with support, pack posted data into active protocol format and broadcasts the PSM. Request body type allows for sending a pre-packed message to be sent as a direct payload or for a JSON format that will be encoded to the appropriate message format and broadcast server side. request ID on success.
[**v2x_rsus_get**](V2XApi.md#v2x_rsus_get) | **GET** /v2x/rsus | Return a list of V2X RSUs known to OCTANE.
[**v2x_rsus_patch**](V2XApi.md#v2x_rsus_patch) | **PATCH** /v2x/rsus | Updates all existing and capable V2x RSUs. Returns request ID on success.

# **v2x_get**
> InlineResponse20047 v2x_get()

Return a list of V2X devices known to OCTANE.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of V2X devices known to OCTANE.
    api_response = api_instance.v2x_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_id_get**
> InlineResponse20050 v2x_id_get(id)

Return a v2x object with the specified ID.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
id = 56 # int | A V2X ID number.

try:
    # Return a v2x object with the specified ID.
    api_response = api_instance.v2x_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A V2X ID number. | 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_id_patch**
> InlineResponse2002 v2x_id_patch(id, body=body)

Updates an existing v2x status, allowing for triggering. Returns request ID on success.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
id = 56 # int | A V2X ID number.
body = swagger_client.Body27() # Body27 |  (optional)

try:
    # Updates an existing v2x status, allowing for triggering. Returns request ID on success.
    api_response = api_instance.v2x_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A V2X ID number. | 
 **body** | [**Body27**](Body27.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_obu_id_get**
> InlineResponse20052 v2x_obu_id_get(id)

Return a v2x object with the specified ID.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
id = 56 # int | A V2X ID number.

try:
    # Return a v2x object with the specified ID.
    api_response = api_instance.v2x_obu_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_obu_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A V2X ID number. | 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_obu_id_patch**
> InlineResponse2002 v2x_obu_id_patch(id, body=body)

Updates an existing v2x status, allowing for triggering. Returns request ID on success.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
id = 56 # int | A V2X ID number.
body = swagger_client.Body29() # Body29 |  (optional)

try:
    # Updates an existing v2x status, allowing for triggering. Returns request ID on success.
    api_response = api_instance.v2x_obu_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_obu_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A V2X ID number. | 
 **body** | [**Body29**](Body29.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_obus_get**
> InlineResponse20049 v2x_obus_get()

Return a list of V2X OBUs known to OCTANE.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of V2X OBUs known to OCTANE.
    api_response = api_instance.v2x_obus_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_obus_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_obus_patch**
> InlineResponse2002 v2x_obus_patch(body=body)

Updates an existing and capable V2X OBUs. Returns request ID on success.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body26() # Body26 |  (optional)

try:
    # Updates an existing and capable V2X OBUs. Returns request ID on success.
    api_response = api_instance.v2x_obus_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_obus_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body26**](Body26.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_rsu_id_bsm_post**
> InlineResponse2002 v2x_rsu_id_bsm_post(id, body=body)

For RSUs with support, pack posted data into active protocol format and broadcasts the BSM.  Request body type allows for sending a pre-packed message to be sent as a direct payload or for a JSON format that will be encoded to the appropriate message format and broadcast serverside. request ID on success.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
id = 56 # int | A V2X ID number.
body = swagger_client.V2XBSM() # V2XBSM |  (optional)

try:
    # For RSUs with support, pack posted data into active protocol format and broadcasts the BSM.  Request body type allows for sending a pre-packed message to be sent as a direct payload or for a JSON format that will be encoded to the appropriate message format and broadcast serverside. request ID on success.
    api_response = api_instance.v2x_rsu_id_bsm_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_rsu_id_bsm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A V2X ID number. | 
 **body** | [**V2XBSM**](V2XBSM.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_rsu_id_bsms_post**
> InlineResponse2005 v2x_rsu_id_bsms_post(id, body=body)

For RSUs with support, pack posted data into active protocol format and broadcasts each row through the BSM. request ID on success.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
id = 56 # int | A V2X ID number.
body = [swagger_client.V2XBSM()] # list[V2XBSM] |  (optional)

try:
    # For RSUs with support, pack posted data into active protocol format and broadcasts each row through the BSM. request ID on success.
    api_response = api_instance.v2x_rsu_id_bsms_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_rsu_id_bsms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A V2X ID number. | 
 **body** | [**list[V2XBSM]**](V2XBSM.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_rsu_id_get**
> InlineResponse20051 v2x_rsu_id_get(id)

Return a v2x object with the specified ID.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
id = 56 # int | A V2X ID number.

try:
    # Return a v2x object with the specified ID.
    api_response = api_instance.v2x_rsu_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_rsu_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A V2X ID number. | 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_rsu_id_patch**
> InlineResponse2002 v2x_rsu_id_patch(id, body=body)

Updates an existing v2x status, allowing for triggering. Returns request ID on success.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
id = 56 # int | A V2X ID number.
body = swagger_client.Body28() # Body28 |  (optional)

try:
    # Updates an existing v2x status, allowing for triggering. Returns request ID on success.
    api_response = api_instance.v2x_rsu_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_rsu_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A V2X ID number. | 
 **body** | [**Body28**](Body28.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_rsu_id_psm_post**
> InlineResponse2002 v2x_rsu_id_psm_post(id, body=body)

For RSUs with support, pack posted data into active protocol format and broadcasts the PSM. Request body type allows for sending a pre-packed message to be sent as a direct payload or for a JSON format that will be encoded to the appropriate message format and broadcast server side. request ID on success.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
id = 56 # int | A V2X RSU ID number.
body = swagger_client.V2XPSM() # V2XPSM |  (optional)

try:
    # For RSUs with support, pack posted data into active protocol format and broadcasts the PSM. Request body type allows for sending a pre-packed message to be sent as a direct payload or for a JSON format that will be encoded to the appropriate message format and broadcast server side. request ID on success.
    api_response = api_instance.v2x_rsu_id_psm_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_rsu_id_psm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A V2X RSU ID number. | 
 **body** | [**V2XPSM**](V2XPSM.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_rsus_get**
> InlineResponse20048 v2x_rsus_get()

Return a list of V2X RSUs known to OCTANE.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of V2X RSUs known to OCTANE.
    api_response = api_instance.v2x_rsus_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_rsus_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2x_rsus_patch**
> InlineResponse2002 v2x_rsus_patch(body=body)

Updates all existing and capable V2x RSUs. Returns request ID on success.

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
api_instance = swagger_client.V2XApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body25() # Body25 |  (optional)

try:
    # Updates all existing and capable V2x RSUs. Returns request ID on success.
    api_response = api_instance.v2x_rsus_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V2XApi->v2x_rsus_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body25**](Body25.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

