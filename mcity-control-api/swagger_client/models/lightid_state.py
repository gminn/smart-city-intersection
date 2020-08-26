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


class LightidState(object):
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
        'enabled': 'bool',
        'dim_level': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'dim_level': 'dimLevel'
    }

    def __init__(self, enabled=None, dim_level=None):  # noqa: E501
        """LightidState - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._dim_level = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if dim_level is not None:
            self.dim_level = dim_level

    @property
    def enabled(self):
        """Gets the enabled of this LightidState.  # noqa: E501

        Default is 0. 1 causes the light to turn on.  # noqa: E501

        :return: The enabled of this LightidState.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this LightidState.

        Default is 0. 1 causes the light to turn on.  # noqa: E501

        :param enabled: The enabled of this LightidState.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def dim_level(self):
        """Gets the dim_level of this LightidState.  # noqa: E501

        Default is 0. > 0 setting toggles the dim percentage of the light.  # noqa: E501

        :return: The dim_level of this LightidState.  # noqa: E501
        :rtype: int
        """
        return self._dim_level

    @dim_level.setter
    def dim_level(self, dim_level):
        """Sets the dim_level of this LightidState.

        Default is 0. > 0 setting toggles the dim percentage of the light.  # noqa: E501

        :param dim_level: The dim_level of this LightidState.  # noqa: E501
        :type: int
        """

        self._dim_level = dim_level

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
        if issubclass(LightidState, dict):
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
        if not isinstance(other, LightidState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
