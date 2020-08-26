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


class APIError(object):
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
        'internal_code': 'int',
        'status': 'int',
        'message': 'str',
        'human_message': 'str'
    }

    attribute_map = {
        'internal_code': 'internalCode',
        'status': 'status',
        'message': 'message',
        'human_message': 'humanMessage'
    }

    def __init__(self, internal_code=None, status=None, message=None, human_message=None):  # noqa: E501
        """APIError - a model defined in Swagger"""  # noqa: E501
        self._internal_code = None
        self._status = None
        self._message = None
        self._human_message = None
        self.discriminator = None
        if internal_code is not None:
            self.internal_code = internal_code
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if human_message is not None:
            self.human_message = human_message

    @property
    def internal_code(self):
        """Gets the internal_code of this APIError.  # noqa: E501

        The internal error code encountered by the API  # noqa: E501

        :return: The internal_code of this APIError.  # noqa: E501
        :rtype: int
        """
        return self._internal_code

    @internal_code.setter
    def internal_code(self, internal_code):
        """Sets the internal_code of this APIError.

        The internal error code encountered by the API  # noqa: E501

        :param internal_code: The internal_code of this APIError.  # noqa: E501
        :type: int
        """

        self._internal_code = internal_code

    @property
    def status(self):
        """Gets the status of this APIError.  # noqa: E501

        The HTTP error code returned with this error object.  # noqa: E501

        :return: The status of this APIError.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this APIError.

        The HTTP error code returned with this error object.  # noqa: E501

        :param status: The status of this APIError.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this APIError.  # noqa: E501

        The error message encountered  # noqa: E501

        :return: The message of this APIError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this APIError.

        The error message encountered  # noqa: E501

        :param message: The message of this APIError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def human_message(self):
        """Gets the human_message of this APIError.  # noqa: E501

        A human readable HTTP error code  # noqa: E501

        :return: The human_message of this APIError.  # noqa: E501
        :rtype: str
        """
        return self._human_message

    @human_message.setter
    def human_message(self, human_message):
        """Sets the human_message of this APIError.

        A human readable HTTP error code  # noqa: E501

        :param human_message: The human_message of this APIError.  # noqa: E501
        :type: str
        """

        self._human_message = human_message

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
        if issubclass(APIError, dict):
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
        if not isinstance(other, APIError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
