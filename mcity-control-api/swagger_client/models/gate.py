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


class Gate(object):
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
        'uri': 'str',
        'name': 'str',
        'url': 'str',
        'longitude': 'float',
        'latitude': 'float',
        'electric': 'bool',
        'arm': 'bool',
        'slide': 'bool',
        'swing': 'bool',
        'lift': 'bool',
        'audible': 'bool',
        'state': 'GateState'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'name': 'name',
        'url': 'url',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'electric': 'electric',
        'arm': 'arm',
        'slide': 'slide',
        'swing': 'swing',
        'lift': 'lift',
        'audible': 'audible',
        'state': 'state'
    }

    def __init__(self, id=None, uri=None, name=None, url=None, longitude=None, latitude=None, electric=None, arm=None, slide=None, swing=None, lift=None, audible=None, state=None):  # noqa: E501
        """Gate - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._uri = None
        self._name = None
        self._url = None
        self._longitude = None
        self._latitude = None
        self._electric = None
        self._arm = None
        self._slide = None
        self._swing = None
        self._lift = None
        self._audible = None
        self._state = None
        self.discriminator = None
        self.id = id
        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if longitude is not None:
            self.longitude = longitude
        if latitude is not None:
            self.latitude = latitude
        if electric is not None:
            self.electric = electric
        if arm is not None:
            self.arm = arm
        if slide is not None:
            self.slide = slide
        if swing is not None:
            self.swing = swing
        if lift is not None:
            self.lift = lift
        if audible is not None:
            self.audible = audible
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this Gate.  # noqa: E501

        An ID number identifying this gate  # noqa: E501

        :return: The id of this Gate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Gate.

        An ID number identifying this gate  # noqa: E501

        :param id: The id of this Gate.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this Gate.  # noqa: E501

        The URI which can be used to access this gate directly  # noqa: E501

        :return: The uri of this Gate.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Gate.

        The URI which can be used to access this gate directly  # noqa: E501

        :param uri: The uri of this Gate.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this Gate.  # noqa: E501

        A text based description of this gate  # noqa: E501

        :return: The name of this Gate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Gate.

        A text based description of this gate  # noqa: E501

        :param name: The name of this Gate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this Gate.  # noqa: E501

        A url with more information about this specific gate  # noqa: E501

        :return: The url of this Gate.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Gate.

        A url with more information about this specific gate  # noqa: E501

        :param url: The url of this Gate.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def longitude(self):
        """Gets the longitude of this Gate.  # noqa: E501

        The longitude of the centroid of the gate  # noqa: E501

        :return: The longitude of this Gate.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Gate.

        The longitude of the centroid of the gate  # noqa: E501

        :param longitude: The longitude of this Gate.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this Gate.  # noqa: E501

        The latitude of the centroid of the gate  # noqa: E501

        :return: The latitude of this Gate.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Gate.

        The latitude of the centroid of the gate  # noqa: E501

        :param latitude: The latitude of this Gate.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def electric(self):
        """Gets the electric of this Gate.  # noqa: E501

        Is this a manual or electric gate  # noqa: E501

        :return: The electric of this Gate.  # noqa: E501
        :rtype: bool
        """
        return self._electric

    @electric.setter
    def electric(self, electric):
        """Sets the electric of this Gate.

        Is this a manual or electric gate  # noqa: E501

        :param electric: The electric of this Gate.  # noqa: E501
        :type: bool
        """

        self._electric = electric

    @property
    def arm(self):
        """Gets the arm of this Gate.  # noqa: E501

        Does this gate have an arm  # noqa: E501

        :return: The arm of this Gate.  # noqa: E501
        :rtype: bool
        """
        return self._arm

    @arm.setter
    def arm(self, arm):
        """Sets the arm of this Gate.

        Does this gate have an arm  # noqa: E501

        :param arm: The arm of this Gate.  # noqa: E501
        :type: bool
        """

        self._arm = arm

    @property
    def slide(self):
        """Gets the slide of this Gate.  # noqa: E501

        Does this gate slide to the side?  # noqa: E501

        :return: The slide of this Gate.  # noqa: E501
        :rtype: bool
        """
        return self._slide

    @slide.setter
    def slide(self, slide):
        """Sets the slide of this Gate.

        Does this gate slide to the side?  # noqa: E501

        :param slide: The slide of this Gate.  # noqa: E501
        :type: bool
        """

        self._slide = slide

    @property
    def swing(self):
        """Gets the swing of this Gate.  # noqa: E501

        Gate swings horizontally to open  # noqa: E501

        :return: The swing of this Gate.  # noqa: E501
        :rtype: bool
        """
        return self._swing

    @swing.setter
    def swing(self, swing):
        """Sets the swing of this Gate.

        Gate swings horizontally to open  # noqa: E501

        :param swing: The swing of this Gate.  # noqa: E501
        :type: bool
        """

        self._swing = swing

    @property
    def lift(self):
        """Gets the lift of this Gate.  # noqa: E501

        Gate lifts to open  # noqa: E501

        :return: The lift of this Gate.  # noqa: E501
        :rtype: bool
        """
        return self._lift

    @lift.setter
    def lift(self, lift):
        """Sets the lift of this Gate.

        Gate lifts to open  # noqa: E501

        :param lift: The lift of this Gate.  # noqa: E501
        :type: bool
        """

        self._lift = lift

    @property
    def audible(self):
        """Gets the audible of this Gate.  # noqa: E501

        Gate has an audible alarm  # noqa: E501

        :return: The audible of this Gate.  # noqa: E501
        :rtype: bool
        """
        return self._audible

    @audible.setter
    def audible(self, audible):
        """Sets the audible of this Gate.

        Gate has an audible alarm  # noqa: E501

        :param audible: The audible of this Gate.  # noqa: E501
        :type: bool
        """

        self._audible = audible

    @property
    def state(self):
        """Gets the state of this Gate.  # noqa: E501


        :return: The state of this Gate.  # noqa: E501
        :rtype: GateState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Gate.


        :param state: The state of this Gate.  # noqa: E501
        :type: GateState
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
        if issubclass(Gate, dict):
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
        if not isinstance(other, Gate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
