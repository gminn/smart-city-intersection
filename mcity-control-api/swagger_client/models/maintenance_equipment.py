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


class MaintenanceEquipment(object):
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
        'name': 'str',
        'state': 'OneOfMaintenanceEquipmentState',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, state=None, type=None):  # noqa: E501
        """MaintenanceEquipment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._state = None
        self._type = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this MaintenanceEquipment.  # noqa: E501

        An ID number identifying this piece of maintenance equipment  # noqa: E501

        :return: The id of this MaintenanceEquipment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MaintenanceEquipment.

        An ID number identifying this piece of maintenance equipment  # noqa: E501

        :param id: The id of this MaintenanceEquipment.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this MaintenanceEquipment.  # noqa: E501

        A text based description of the maintenance equipment.  # noqa: E501

        :return: The name of this MaintenanceEquipment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MaintenanceEquipment.

        A text based description of the maintenance equipment.  # noqa: E501

        :param name: The name of this MaintenanceEquipment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this MaintenanceEquipment.  # noqa: E501

        The current state of the maintenance device  # noqa: E501

        :return: The state of this MaintenanceEquipment.  # noqa: E501
        :rtype: OneOfMaintenanceEquipmentState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MaintenanceEquipment.

        The current state of the maintenance device  # noqa: E501

        :param state: The state of this MaintenanceEquipment.  # noqa: E501
        :type: OneOfMaintenanceEquipmentState
        """

        self._state = state

    @property
    def type(self):
        """Gets the type of this MaintenanceEquipment.  # noqa: E501

        The maintenance equipment type  # noqa: E501

        :return: The type of this MaintenanceEquipment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MaintenanceEquipment.

        The maintenance equipment type  # noqa: E501

        :param type: The type of this MaintenanceEquipment.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(MaintenanceEquipment, dict):
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
        if not isinstance(other, MaintenanceEquipment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
