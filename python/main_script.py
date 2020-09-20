from __future__ import print_function
import time
import swagger_client
import Intersection
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY' # <---- CHANGE THIS EACH TESTING SESSION
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SignalsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A signal ID string. <---- CHANGE THIS

try:
    # Return an signal object with the specified ID.
    api_response = api_instance.signal_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignalsApi->signal_id_get: %s\n" % e)
