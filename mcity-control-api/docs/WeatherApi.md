# swagger_client.WeatherApi

All URIs are relative to *https://mcity.um.city/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**weather_alerts_current_get**](WeatherApi.md#weather_alerts_current_get) | **GET** /weather/alerts/current | Return the current weather alert
[**weather_alerts_date_get**](WeatherApi.md#weather_alerts_date_get) | **GET** /weather/alerts/{date} | Return a list of weather alerts from given date

# **weather_alerts_current_get**
> InlineResponse20026 weather_alerts_current_get()

Return the current weather alert

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
api_instance = swagger_client.WeatherApi(swagger_client.ApiClient(configuration))

try:
    # Return the current weather alert
    api_response = api_instance.weather_alerts_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherApi->weather_alerts_current_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **weather_alerts_date_get**
> InlineResponse20026 weather_alerts_date_get(_date)

Return a list of weather alerts from given date

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
api_instance = swagger_client.WeatherApi(swagger_client.ApiClient(configuration))
_date = '_date_example' # str | YYYY-MM-DD

try:
    # Return a list of weather alerts from given date
    api_response = api_instance.weather_alerts_date_get(_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WeatherApi->weather_alerts_date_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_date** | **str**| YYYY-MM-DD | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

