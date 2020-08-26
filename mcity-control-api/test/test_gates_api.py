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
from api.gates_api import GatesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGatesApi(unittest.TestCase):
    """GatesApi unit test stubs"""

    def setUp(self):
        self.api = api.gates_api.GatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_gate_id_get(self):
        """Test case for gate_id_get

        Return a gate object with the specified ID.  # noqa: E501
        """
        pass

    def test_gate_id_patch(self):
        """Test case for gate_id_patch

        Updates an existing gate status, allowing for triggering. Returns request ID on success.  # noqa: E501
        """
        pass

    def test_gates_get(self):
        """Test case for gates_get

        Return a list of gate objects describing all instrumented gates within the facility.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
