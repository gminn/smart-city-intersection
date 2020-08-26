# swagger_client.ScenariosApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scenario_id_delete**](ScenariosApi.md#scenario_id_delete) | **DELETE** /scenario/{id} | Delete a scenario from the database
[**scenario_id_get**](ScenariosApi.md#scenario_id_get) | **GET** /scenario/{id} | Return a scenario object with the specified id
[**scenario_id_patch**](ScenariosApi.md#scenario_id_patch) | **PATCH** /scenario/{id} | Update an existing scenario
[**scenario_post**](ScenariosApi.md#scenario_post) | **POST** /scenario | Create a new scenario object
[**scenarios_get**](ScenariosApi.md#scenarios_get) | **GET** /scenarios | Return a list of scenario objects.

# **scenario_id_delete**
> InlineResponse20056 scenario_id_delete(id)

Delete a scenario from the database

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
api_instance = swagger_client.ScenariosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A scenario id string.

try:
    # Delete a scenario from the database
    api_response = api_instance.scenario_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenariosApi->scenario_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A scenario id string. | 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenario_id_get**
> InlineResponse20064 scenario_id_get(id)

Return a scenario object with the specified id

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
api_instance = swagger_client.ScenariosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A scenario id string.

try:
    # Return a scenario object with the specified id
    api_response = api_instance.scenario_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenariosApi->scenario_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A scenario id string. | 

### Return type

[**InlineResponse20064**](InlineResponse20064.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenario_id_patch**
> InlineResponse20065 scenario_id_patch(id, body=body)

Update an existing scenario

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
api_instance = swagger_client.ScenariosApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A scenario id string.
body = swagger_client.Body41() # Body41 |  (optional)

try:
    # Update an existing scenario
    api_response = api_instance.scenario_id_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenariosApi->scenario_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A scenario id string. | 
 **body** | [**Body41**](Body41.md)|  | [optional] 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenario_post**
> InlineResponse20065 scenario_post(body=body)

Create a new scenario object

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
api_instance = swagger_client.ScenariosApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body42() # Body42 |  (optional)

try:
    # Create a new scenario object
    api_response = api_instance.scenario_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenariosApi->scenario_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body42**](Body42.md)|  | [optional] 

### Return type

[**InlineResponse20065**](InlineResponse20065.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scenarios_get**
> InlineResponse20063 scenarios_get()

Return a list of scenario objects.

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
api_instance = swagger_client.ScenariosApi(swagger_client.ApiClient(configuration))

try:
    # Return a list of scenario objects.
    api_response = api_instance.scenarios_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScenariosApi->scenarios_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

