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


class SensorRADAR(object):
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
        'manufacturer': 'str',
        'model': 'str',
        'revision': 'str',
        'ip_address': 'str',
        'url_web_interface': 'str',
        'range_max': 'float',
        'range_accuracy': 'float',
        'speed_accuracy': 'float',
        'resolution_update_rate': 'float',
        'objected_tracked_max': 'int',
        'state': 'SensorState'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'name': 'name',
        'url': 'url',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'type': 'type',
        'manufacturer': 'manufacturer',
        'model': 'model',
        'revision': 'revision',
        'ip_address': 'ipAddress',
        'url_web_interface': 'urlWebInterface',
        'range_max': 'rangeMax',
        'range_accuracy': 'rangeAccuracy',
        'speed_accuracy': 'speedAccuracy',
        'resolution_update_rate': 'resolutionUpdateRate',
        'objected_tracked_max': 'objectedTrackedMax',
        'state': 'state'
    }

    def __init__(self, id=None, uri=None, name=None, url=None, longitude=None, latitude=None, type=None, manufacturer=None, model=None, revision=None, ip_address=None, url_web_interface=None, range_max=None, range_accuracy=None, speed_accuracy=None, resolution_update_rate=None, objected_tracked_max=None, state=None):  # noqa: E501
        """SensorRADAR - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._uri = None
        self._name = None
        self._url = None
        self._longitude = None
        self._latitude = None
        self._type = None
        self._manufacturer = None
        self._model = None
        self._revision = None
        self._ip_address = None
        self._url_web_interface = None
        self._range_max = None
        self._range_accuracy = None
        self._speed_accuracy = None
        self._resolution_update_rate = None
        self._objected_tracked_max = None
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
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if model is not None:
            self.model = model
        if revision is not None:
            self.revision = revision
        if ip_address is not None:
            self.ip_address = ip_address
        if url_web_interface is not None:
            self.url_web_interface = url_web_interface
        if range_max is not None:
            self.range_max = range_max
        if range_accuracy is not None:
            self.range_accuracy = range_accuracy
        if speed_accuracy is not None:
            self.speed_accuracy = speed_accuracy
        if resolution_update_rate is not None:
            self.resolution_update_rate = resolution_update_rate
        if objected_tracked_max is not None:
            self.objected_tracked_max = objected_tracked_max
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this SensorRADAR.  # noqa: E501

        An ID number identifying this sensor  # noqa: E501

        :return: The id of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SensorRADAR.

        An ID number identifying this sensor  # noqa: E501

        :param id: The id of this SensorRADAR.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this SensorRADAR.  # noqa: E501

        The URI which can be used to access this sensor  # noqa: E501

        :return: The uri of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this SensorRADAR.

        The URI which can be used to access this sensor  # noqa: E501

        :param uri: The uri of this SensorRADAR.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this SensorRADAR.  # noqa: E501

        A text based description of the sensor  # noqa: E501

        :return: The name of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SensorRADAR.

        A text based description of the sensor  # noqa: E501

        :param name: The name of this SensorRADAR.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this SensorRADAR.  # noqa: E501

        A url with more information about this specific sensor  # noqa: E501

        :return: The url of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SensorRADAR.

        A url with more information about this specific sensor  # noqa: E501

        :param url: The url of this SensorRADAR.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def longitude(self):
        """Gets the longitude of this SensorRADAR.  # noqa: E501

        The longitude of the centroid of the sensor  # noqa: E501

        :return: The longitude of this SensorRADAR.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this SensorRADAR.

        The longitude of the centroid of the sensor  # noqa: E501

        :param longitude: The longitude of this SensorRADAR.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this SensorRADAR.  # noqa: E501

        The latitude of the centroid of the sensor  # noqa: E501

        :return: The latitude of this SensorRADAR.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this SensorRADAR.

        The latitude of the centroid of the sensor  # noqa: E501

        :param latitude: The latitude of this SensorRADAR.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def type(self):
        """Gets the type of this SensorRADAR.  # noqa: E501

        The sensor type  # noqa: E501

        :return: The type of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SensorRADAR.

        The sensor type  # noqa: E501

        :param type: The type of this SensorRADAR.  # noqa: E501
        :type: str
        """
        allowed_values = ["RADAR"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def manufacturer(self):
        """Gets the manufacturer of this SensorRADAR.  # noqa: E501

        The sensor manufacturer  # noqa: E501

        :return: The manufacturer of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this SensorRADAR.

        The sensor manufacturer  # noqa: E501

        :param manufacturer: The manufacturer of this SensorRADAR.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def model(self):
        """Gets the model of this SensorRADAR.  # noqa: E501

        The model number/name of the sensor  # noqa: E501

        :return: The model of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this SensorRADAR.

        The model number/name of the sensor  # noqa: E501

        :param model: The model of this SensorRADAR.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """Gets the revision of this SensorRADAR.  # noqa: E501

        Sensor revision number/edition information  # noqa: E501

        :return: The revision of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this SensorRADAR.

        Sensor revision number/edition information  # noqa: E501

        :param revision: The revision of this SensorRADAR.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def ip_address(self):
        """Gets the ip_address of this SensorRADAR.  # noqa: E501

        The IP Address of the sensor  # noqa: E501

        :return: The ip_address of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this SensorRADAR.

        The IP Address of the sensor  # noqa: E501

        :param ip_address: The ip_address of this SensorRADAR.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def url_web_interface(self):
        """Gets the url_web_interface of this SensorRADAR.  # noqa: E501

        A URL allowing control or management of the sensor  # noqa: E501

        :return: The url_web_interface of this SensorRADAR.  # noqa: E501
        :rtype: str
        """
        return self._url_web_interface

    @url_web_interface.setter
    def url_web_interface(self, url_web_interface):
        """Sets the url_web_interface of this SensorRADAR.

        A URL allowing control or management of the sensor  # noqa: E501

        :param url_web_interface: The url_web_interface of this SensorRADAR.  # noqa: E501
        :type: str
        """

        self._url_web_interface = url_web_interface

    @property
    def range_max(self):
        """Gets the range_max of this SensorRADAR.  # noqa: E501

        The maximum range of the sensor.  # noqa: E501

        :return: The range_max of this SensorRADAR.  # noqa: E501
        :rtype: float
        """
        return self._range_max

    @range_max.setter
    def range_max(self, range_max):
        """Sets the range_max of this SensorRADAR.

        The maximum range of the sensor.  # noqa: E501

        :param range_max: The range_max of this SensorRADAR.  # noqa: E501
        :type: float
        """

        self._range_max = range_max

    @property
    def range_accuracy(self):
        """Gets the range_accuracy of this SensorRADAR.  # noqa: E501

        The accuracy range rating of the sensor.  # noqa: E501

        :return: The range_accuracy of this SensorRADAR.  # noqa: E501
        :rtype: float
        """
        return self._range_accuracy

    @range_accuracy.setter
    def range_accuracy(self, range_accuracy):
        """Sets the range_accuracy of this SensorRADAR.

        The accuracy range rating of the sensor.  # noqa: E501

        :param range_accuracy: The range_accuracy of this SensorRADAR.  # noqa: E501
        :type: float
        """

        self._range_accuracy = range_accuracy

    @property
    def speed_accuracy(self):
        """Gets the speed_accuracy of this SensorRADAR.  # noqa: E501

        The accuracy of speed detection of the sensor  # noqa: E501

        :return: The speed_accuracy of this SensorRADAR.  # noqa: E501
        :rtype: float
        """
        return self._speed_accuracy

    @speed_accuracy.setter
    def speed_accuracy(self, speed_accuracy):
        """Sets the speed_accuracy of this SensorRADAR.

        The accuracy of speed detection of the sensor  # noqa: E501

        :param speed_accuracy: The speed_accuracy of this SensorRADAR.  # noqa: E501
        :type: float
        """

        self._speed_accuracy = speed_accuracy

    @property
    def resolution_update_rate(self):
        """Gets the resolution_update_rate of this SensorRADAR.  # noqa: E501

        The rate at which the sensor updates.  # noqa: E501

        :return: The resolution_update_rate of this SensorRADAR.  # noqa: E501
        :rtype: float
        """
        return self._resolution_update_rate

    @resolution_update_rate.setter
    def resolution_update_rate(self, resolution_update_rate):
        """Sets the resolution_update_rate of this SensorRADAR.

        The rate at which the sensor updates.  # noqa: E501

        :param resolution_update_rate: The resolution_update_rate of this SensorRADAR.  # noqa: E501
        :type: float
        """

        self._resolution_update_rate = resolution_update_rate

    @property
    def objected_tracked_max(self):
        """Gets the objected_tracked_max of this SensorRADAR.  # noqa: E501

        The maximum number of objects tracked by the sensor.  # noqa: E501

        :return: The objected_tracked_max of this SensorRADAR.  # noqa: E501
        :rtype: int
        """
        return self._objected_tracked_max

    @objected_tracked_max.setter
    def objected_tracked_max(self, objected_tracked_max):
        """Sets the objected_tracked_max of this SensorRADAR.

        The maximum number of objects tracked by the sensor.  # noqa: E501

        :param objected_tracked_max: The objected_tracked_max of this SensorRADAR.  # noqa: E501
        :type: int
        """

        self._objected_tracked_max = objected_tracked_max

    @property
    def state(self):
        """Gets the state of this SensorRADAR.  # noqa: E501


        :return: The state of this SensorRADAR.  # noqa: E501
        :rtype: SensorState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SensorRADAR.


        :param state: The state of this SensorRADAR.  # noqa: E501
        :type: SensorState
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
        if issubclass(SensorRADAR, dict):
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
        if not isinstance(other, SensorRADAR):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
