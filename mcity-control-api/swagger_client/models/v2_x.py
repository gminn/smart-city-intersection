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


class V2X(object):
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
        'type': 'str',
        'radios_supported': 'list[V2XRadiosSupported]',
        'manufacturer': 'str',
        'model': 'str',
        'revision': 'str',
        'vehicle_manufacturer': 'str',
        'vehicle_model': 'str',
        'vehicle_year': 'str',
        'state': 'V2XState'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'name': 'name',
        'url': 'url',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'type': 'type',
        'radios_supported': 'radiosSupported',
        'manufacturer': 'manufacturer',
        'model': 'model',
        'revision': 'revision',
        'vehicle_manufacturer': 'vehicleManufacturer',
        'vehicle_model': 'vehicleModel',
        'vehicle_year': 'vehicleYear',
        'state': 'state'
    }

    def __init__(self, id=None, uri=None, name=None, url=None, longitude=None, latitude=None, type=None, radios_supported=None, manufacturer=None, model=None, revision=None, vehicle_manufacturer=None, vehicle_model=None, vehicle_year=None, state=None):  # noqa: E501
        """V2X - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._uri = None
        self._name = None
        self._url = None
        self._longitude = None
        self._latitude = None
        self._type = None
        self._radios_supported = None
        self._manufacturer = None
        self._model = None
        self._revision = None
        self._vehicle_manufacturer = None
        self._vehicle_model = None
        self._vehicle_year = None
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
        if type is not None:
            self.type = type
        if radios_supported is not None:
            self.radios_supported = radios_supported
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if model is not None:
            self.model = model
        if revision is not None:
            self.revision = revision
        if vehicle_manufacturer is not None:
            self.vehicle_manufacturer = vehicle_manufacturer
        if vehicle_model is not None:
            self.vehicle_model = vehicle_model
        if vehicle_year is not None:
            self.vehicle_year = vehicle_year
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this V2X.  # noqa: E501

        An ID number identifying this V2X device  # noqa: E501

        :return: The id of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2X.

        An ID number identifying this V2X device  # noqa: E501

        :param id: The id of this V2X.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this V2X.  # noqa: E501

        The URI which can be used to access this V2X device directly  # noqa: E501

        :return: The uri of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this V2X.

        The URI which can be used to access this V2X device directly  # noqa: E501

        :param uri: The uri of this V2X.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this V2X.  # noqa: E501

        A text based description of this V2X device  # noqa: E501

        :return: The name of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2X.

        A text based description of this V2X device  # noqa: E501

        :param name: The name of this V2X.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this V2X.  # noqa: E501

        A url with more information about this specific V2X device  # noqa: E501

        :return: The url of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V2X.

        A url with more information about this specific V2X device  # noqa: E501

        :param url: The url of this V2X.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def longitude(self):
        """Gets the longitude of this V2X.  # noqa: E501

        The longitude of the centroid of the V2X device, if fixed.  # noqa: E501

        :return: The longitude of this V2X.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this V2X.

        The longitude of the centroid of the V2X device, if fixed.  # noqa: E501

        :param longitude: The longitude of this V2X.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this V2X.  # noqa: E501

        The latitude of the centroid of the V2X device, if fixed.  # noqa: E501

        :return: The latitude of this V2X.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this V2X.

        The latitude of the centroid of the V2X device, if fixed.  # noqa: E501

        :param latitude: The latitude of this V2X.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def type(self):
        """Gets the type of this V2X.  # noqa: E501


        :return: The type of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V2X.


        :param type: The type of this V2X.  # noqa: E501
        :type: str
        """
        allowed_values = ["OBU", "RSU"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def radios_supported(self):
        """Gets the radios_supported of this V2X.  # noqa: E501

        A list of supported configurations for this device.  # noqa: E501

        :return: The radios_supported of this V2X.  # noqa: E501
        :rtype: list[V2XRadiosSupported]
        """
        return self._radios_supported

    @radios_supported.setter
    def radios_supported(self, radios_supported):
        """Sets the radios_supported of this V2X.

        A list of supported configurations for this device.  # noqa: E501

        :param radios_supported: The radios_supported of this V2X.  # noqa: E501
        :type: list[V2XRadiosSupported]
        """

        self._radios_supported = radios_supported

    @property
    def manufacturer(self):
        """Gets the manufacturer of this V2X.  # noqa: E501

        The OBU/RSU manufacturer  # noqa: E501

        :return: The manufacturer of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this V2X.

        The OBU/RSU manufacturer  # noqa: E501

        :param manufacturer: The manufacturer of this V2X.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def model(self):
        """Gets the model of this V2X.  # noqa: E501

        The OBU/RSU model  # noqa: E501

        :return: The model of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this V2X.

        The OBU/RSU model  # noqa: E501

        :param model: The model of this V2X.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """Gets the revision of this V2X.  # noqa: E501

        Revision of the OBU/RSU  # noqa: E501

        :return: The revision of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this V2X.

        Revision of the OBU/RSU  # noqa: E501

        :param revision: The revision of this V2X.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def vehicle_manufacturer(self):
        """Gets the vehicle_manufacturer of this V2X.  # noqa: E501

        Manufacturer of vehicle  # noqa: E501

        :return: The vehicle_manufacturer of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_manufacturer

    @vehicle_manufacturer.setter
    def vehicle_manufacturer(self, vehicle_manufacturer):
        """Sets the vehicle_manufacturer of this V2X.

        Manufacturer of vehicle  # noqa: E501

        :param vehicle_manufacturer: The vehicle_manufacturer of this V2X.  # noqa: E501
        :type: str
        """

        self._vehicle_manufacturer = vehicle_manufacturer

    @property
    def vehicle_model(self):
        """Gets the vehicle_model of this V2X.  # noqa: E501

        Model of vehicle  # noqa: E501

        :return: The vehicle_model of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_model

    @vehicle_model.setter
    def vehicle_model(self, vehicle_model):
        """Sets the vehicle_model of this V2X.

        Model of vehicle  # noqa: E501

        :param vehicle_model: The vehicle_model of this V2X.  # noqa: E501
        :type: str
        """

        self._vehicle_model = vehicle_model

    @property
    def vehicle_year(self):
        """Gets the vehicle_year of this V2X.  # noqa: E501

        Release year of Vehicle.  # noqa: E501

        :return: The vehicle_year of this V2X.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_year

    @vehicle_year.setter
    def vehicle_year(self, vehicle_year):
        """Sets the vehicle_year of this V2X.

        Release year of Vehicle.  # noqa: E501

        :param vehicle_year: The vehicle_year of this V2X.  # noqa: E501
        :type: str
        """

        self._vehicle_year = vehicle_year

    @property
    def state(self):
        """Gets the state of this V2X.  # noqa: E501


        :return: The state of this V2X.  # noqa: E501
        :rtype: V2XState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V2X.


        :param state: The state of this V2X.  # noqa: E501
        :type: V2XState
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
        if issubclass(V2X, dict):
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
        if not isinstance(other, V2X):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
