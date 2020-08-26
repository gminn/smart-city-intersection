# coding: utf-8

"""
    Mcity Control API

    Mcity implementation of OCTANE RESTful/Websocket API designed for autonomous and connected vehicle test facilities/cities.  # noqa: E501

    OpenAPI spec version: 0.0.10
    Contact: mcity-engineering@umich.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.signals_api import SignalsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSignalsApi(unittest.TestCase):
    """SignalsApi unit test stubs"""

    def setUp(self):
        self.api = api.signals_api.SignalsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_signal_id_get(self):
        """Test case for signal_id_get

        Return an signal object with the specified ID.  # noqa: E501
        """
        pass

    def test_signal_id_patch(self):
        """Test case for signal_id_patch

        Allows control of a single signal set.  # noqa: E501
        """
        pass

    def test_signals_get(self):
        """Test case for signals_get

        Return a list of signal objects describing all instrumented signals within the facility.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
