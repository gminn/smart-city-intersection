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


class InlineResponse2003(object):
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
        'id': 'str',
        'serviced': 'datetime',
        'state': 'GarageState'
    }

    attribute_map = {
        'id': 'id',
        'serviced': 'serviced',
        'state': 'state'
    }

    def __init__(self, id=None, serviced=None, state=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._serviced = None
        self._state = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if serviced is not None:
            self.serviced = serviced
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this InlineResponse2003.  # noqa: E501

        An ID number identifying this light fixture.  # noqa: E501

        :return: The id of this InlineResponse2003.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2003.

        An ID number identifying this light fixture.  # noqa: E501

        :param id: The id of this InlineResponse2003.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def serviced(self):
        """Gets the serviced of this InlineResponse2003.  # noqa: E501

        UTC date time representing when the message was published.  # noqa: E501

        :return: The serviced of this InlineResponse2003.  # noqa: E501
        :rtype: datetime
        """
        return self._serviced

    @serviced.setter
    def serviced(self, serviced):
        """Sets the serviced of this InlineResponse2003.

        UTC date time representing when the message was published.  # noqa: E501

        :param serviced: The serviced of this InlineResponse2003.  # noqa: E501
        :type: datetime
        """

        self._serviced = serviced

    @property
    def state(self):
        """Gets the state of this InlineResponse2003.  # noqa: E501


        :return: The state of this InlineResponse2003.  # noqa: E501
        :rtype: GarageState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineResponse2003.


        :param state: The state of this InlineResponse2003.  # noqa: E501
        :type: GarageState
        """

        self._state = state

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
        if issubclass(InlineResponse2003, dict):
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
        if not isinstance(other, InlineResponse2003):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
