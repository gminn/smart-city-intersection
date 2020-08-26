# coding: utf-8

"""
    Mcity Control API

    Mcity implementation of OCTANE RESTful/Websocket API designed for autonomous and connected vehicle test facilities/cities.  # noqa: E501

    OpenAPI spec version: 0.0.10
    Contact: mcity-engineering@umich.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def management_device_callback_post(self, **kwargs):  # noqa: E501
        """TOKEN TYPE: DEVICE. Handles callbacks from physical devices connected to API.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_device_callback_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body35 body: External devices use this to modify state of API managed device state.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.management_device_callback_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.management_device_callback_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def management_device_callback_post_with_http_info(self, **kwargs):  # noqa: E501
        """TOKEN TYPE: DEVICE. Handles callbacks from physical devices connected to API.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_device_callback_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body35 body: External devices use this to modify state of API managed device state.
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method management_device_callback_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/management/device/callback', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def management_facility_reset_post(self, **kwargs):  # noqa: E501
        """TOKEN TYPE: USER. Reset controllable items within the facility.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_facility_reset_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body34 body: Modify the state of all devices in the facility
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.management_facility_reset_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.management_facility_reset_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def management_facility_reset_post_with_http_info(self, **kwargs):  # noqa: E501
        """TOKEN TYPE: USER. Reset controllable items within the facility.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_facility_reset_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body34 body: Modify the state of all devices in the facility
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method management_facility_reset_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/management/facility/reset', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def management_favorite_module_name_favorite_id_delete(self, module_name, favorite_id, **kwargs):  # noqa: E501
        """Delete a favorite from the database.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_favorite_module_name_favorite_id_delete(module_name, favorite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_name: Type of infrastructure (required)
        :param int favorite_id: Type of infrastructure id (required)
        :return: InlineResponse20056
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.management_favorite_module_name_favorite_id_delete_with_http_info(module_name, favorite_id, **kwargs)  # noqa: E501
        else:
            (data) = self.management_favorite_module_name_favorite_id_delete_with_http_info(module_name, favorite_id, **kwargs)  # noqa: E501
            return data

    def management_favorite_module_name_favorite_id_delete_with_http_info(self, module_name, favorite_id, **kwargs):  # noqa: E501
        """Delete a favorite from the database.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_favorite_module_name_favorite_id_delete_with_http_info(module_name, favorite_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str module_name: Type of infrastructure (required)
        :param int favorite_id: Type of infrastructure id (required)
        :return: InlineResponse20056
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['module_name', 'favorite_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method management_favorite_module_name_favorite_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'module_name' is set
        if ('module_name' not in params or
                params['module_name'] is None):
            raise ValueError("Missing the required parameter `module_name` when calling `management_favorite_module_name_favorite_id_delete`")  # noqa: E501
        # verify the required parameter 'favorite_id' is set
        if ('favorite_id' not in params or
                params['favorite_id'] is None):
            raise ValueError("Missing the required parameter `favorite_id` when calling `management_favorite_module_name_favorite_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'module_name' in params:
            path_params['moduleName'] = params['module_name']  # noqa: E501
        if 'favorite_id' in params:
            path_params['favoriteId'] = params['favorite_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/management/favorite/{moduleName}/{favoriteId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20056',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def management_favorite_post(self, **kwargs):  # noqa: E501
        """Add a favorite to database.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_favorite_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body32 body:
        :return: Favorite
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.management_favorite_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.management_favorite_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def management_favorite_post_with_http_info(self, **kwargs):  # noqa: E501
        """Add a favorite to database.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_favorite_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body32 body:
        :return: Favorite
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method management_favorite_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/management/favorite', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Favorite',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def management_favorites_get(self, **kwargs):  # noqa: E501
        """Retrieve list of all favorites.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_favorites_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20055
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.management_favorites_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.management_favorites_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def management_favorites_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve list of all favorites.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_favorites_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20055
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method management_favorites_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/management/favorites', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20055',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def management_modules_get(self, **kwargs):  # noqa: E501
        """Return a list of Modules supported by this instance of Octane  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_modules_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20054
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.management_modules_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.management_modules_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def management_modules_get_with_http_info(self, **kwargs):  # noqa: E501
        """Return a list of Modules supported by this instance of Octane  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_modules_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20054
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method management_modules_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/management/modules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20054',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def management_polling_intersections_patch(self, **kwargs):  # noqa: E501
        """TOKEN TYPE: ADMIN. Start/Stop Intersection Traffic signal polling.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_polling_intersections_patch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body33 body: Modifications to the process that controls intersection updates
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.management_polling_intersections_patch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.management_polling_intersections_patch_with_http_info(**kwargs)  # noqa: E501
            return data

    def management_polling_intersections_patch_with_http_info(self, **kwargs):  # noqa: E501
        """TOKEN TYPE: ADMIN. Start/Stop Intersection Traffic signal polling.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.management_polling_intersections_patch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body33 body: Modifications to the process that controls intersection updates
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method management_polling_intersections_patch" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/management/polling/intersections', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
