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


class SignBoardState(object):
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
        'content_type': 'str',
        'content': 'str',
        'longitude': 'float',
        'latitude': 'float'
    }

    attribute_map = {
        'content_type': 'contentType',
        'content': 'content',
        'longitude': 'longitude',
        'latitude': 'latitude'
    }

    def __init__(self, content_type=None, content=None, longitude=None, latitude=None):  # noqa: E501
        """SignBoardState - a model defined in Swagger"""  # noqa: E501
        self._content_type = None
        self._content = None
        self._longitude = None
        self._latitude = None
        self.discriminator = None
        if content_type is not None:
            self.content_type = content_type
        if content is not None:
            self.content = content
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude

    @property
    def content_type(self):
        """Gets the content_type of this SignBoardState.  # noqa: E501

        The current content type ('text' or 'pattern') of the sign board  # noqa: E501

        :return: The content_type of this SignBoardState.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this SignBoardState.

        The current content type ('text' or 'pattern') of the sign board  # noqa: E501

        :param content_type: The content_type of this SignBoardState.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def content(self):
        """Gets the content of this SignBoardState.  # noqa: E501

        The current content of the sign board  # noqa: E501

        :return: The content of this SignBoardState.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this SignBoardState.

        The current content of the sign board  # noqa: E501

        :param content: The content of this SignBoardState.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def longitude(self):
        """Gets the longitude of this SignBoardState.  # noqa: E501

        The longitude of the centroid of the sign board  # noqa: E501

        :return: The longitude of this SignBoardState.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this SignBoardState.

        The longitude of the centroid of the sign board  # noqa: E501

        :param longitude: The longitude of this SignBoardState.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this SignBoardState.  # noqa: E501

        The latitude of the centroid of the sign board  # noqa: E501

        :return: The latitude of this SignBoardState.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this SignBoardState.

        The latitude of the centroid of the sign board  # noqa: E501

        :param latitude: The latitude of this SignBoardState.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

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
        if issubclass(SignBoardState, dict):
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
        if not isinstance(other, SignBoardState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
