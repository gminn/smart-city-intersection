# coding: utf-8

"""
    Mcity Control API

    Mcity implementation of OCTANE RESTful/Websocket API designed for autonomous and connected vehicle test facilities/cities.  # noqa: E501

    OpenAPI spec version: 0.0.10
    Contact: mcity-engineering@umich.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class MaintenancelawnmoweridState(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mower_call': 'str'
    }

    attribute_map = {
        'mower_call': 'mowerCall'
    }

    def __init__(self, mower_call=None):  # noqa: E501
        """MaintenancelawnmoweridState - a model defined in Swagger"""  # noqa: E501
        self._mower_call = None
        self.discriminator = None
        if mower_call is not None:
            self.mower_call = mower_call

    @property
    def mower_call(self):
        """Gets the mower_call of this MaintenancelawnmoweridState.  # noqa: E501

        Change the mowing state of the mower (start or stop)  # noqa: E501

        :return: The mower_call of this MaintenancelawnmoweridState.  # noqa: E501
        :rtype: str
        """
        return self._mower_call

    @mower_call.setter
    def mower_call(self, mower_call):
        """Sets the mower_call of this MaintenancelawnmoweridState.

        Change the mowing state of the mower (start or stop)  # noqa: E501

        :param mower_call: The mower_call of this MaintenancelawnmoweridState.  # noqa: E501
        :type: str
        """

        self._mower_call = mower_call

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MaintenancelawnmoweridState, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MaintenancelawnmoweridState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
