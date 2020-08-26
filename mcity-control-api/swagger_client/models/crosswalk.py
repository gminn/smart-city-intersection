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


class Crosswalk(object):
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
        'instrument': 'str',
        'refuge': 'bool',
        'beacon': 'str',
        'phases': 'list[str]',
        'countdown': 'bool',
        'audible': 'bool',
        'visor': 'str',
        'call_button': 'bool',
        'tactile_surface': 'bool',
        'state': 'CrosswalkState'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'name': 'name',
        'url': 'url',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'instrument': 'instrument',
        'refuge': 'refuge',
        'beacon': 'beacon',
        'phases': 'phases',
        'countdown': 'countdown',
        'audible': 'audible',
        'visor': 'visor',
        'call_button': 'callButton',
        'tactile_surface': 'tactileSurface',
        'state': 'state'
    }

    def __init__(self, id=None, uri=None, name=None, url=None, longitude=None, latitude=None, instrument=None, refuge=None, beacon=None, phases=None, countdown=None, audible=None, visor=None, call_button=None, tactile_surface=None, state=None):  # noqa: E501
        """Crosswalk - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._uri = None
        self._name = None
        self._url = None
        self._longitude = None
        self._latitude = None
        self._instrument = None
        self._refuge = None
        self._beacon = None
        self._phases = None
        self._countdown = None
        self._audible = None
        self._visor = None
        self._call_button = None
        self._tactile_surface = None
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
        if instrument is not None:
            self.instrument = instrument
        if refuge is not None:
            self.refuge = refuge
        if beacon is not None:
            self.beacon = beacon
        if phases is not None:
            self.phases = phases
        if countdown is not None:
            self.countdown = countdown
        if audible is not None:
            self.audible = audible
        if visor is not None:
            self.visor = visor
        if call_button is not None:
            self.call_button = call_button
        if tactile_surface is not None:
            self.tactile_surface = tactile_surface
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this Crosswalk.  # noqa: E501

        An ID number identifying this crosswalk  # noqa: E501

        :return: The id of this Crosswalk.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Crosswalk.

        An ID number identifying this crosswalk  # noqa: E501

        :param id: The id of this Crosswalk.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this Crosswalk.  # noqa: E501

        The URI which can be used to access this crosswalk directly  # noqa: E501

        :return: The uri of this Crosswalk.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Crosswalk.

        The URI which can be used to access this crosswalk directly  # noqa: E501

        :param uri: The uri of this Crosswalk.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this Crosswalk.  # noqa: E501

        A text based description of this crosswalk  # noqa: E501

        :return: The name of this Crosswalk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Crosswalk.

        A text based description of this crosswalk  # noqa: E501

        :param name: The name of this Crosswalk.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this Crosswalk.  # noqa: E501

        A url with more information about this specific crosswalk  # noqa: E501

        :return: The url of this Crosswalk.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Crosswalk.

        A url with more information about this specific crosswalk  # noqa: E501

        :param url: The url of this Crosswalk.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def longitude(self):
        """Gets the longitude of this Crosswalk.  # noqa: E501

        The longitude of the centroid of the crosswalk  # noqa: E501

        :return: The longitude of this Crosswalk.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Crosswalk.

        The longitude of the centroid of the crosswalk  # noqa: E501

        :param longitude: The longitude of this Crosswalk.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this Crosswalk.  # noqa: E501

        The latitude of the centroid of the crosswalk  # noqa: E501

        :return: The latitude of this Crosswalk.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Crosswalk.

        The latitude of the centroid of the crosswalk  # noqa: E501

        :param latitude: The latitude of this Crosswalk.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def instrument(self):
        """Gets the instrument of this Crosswalk.  # noqa: E501

        The painted line pattern for this crosswalk  # noqa: E501

        :return: The instrument of this Crosswalk.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this Crosswalk.

        The painted line pattern for this crosswalk  # noqa: E501

        :param instrument: The instrument of this Crosswalk.  # noqa: E501
        :type: str
        """
        allowed_values = ["solid", "standard", "continental", "dashed", "ladder", "zebra", "scramble", "uk-pelican", "uk-puffin", "uk-toucan", "uk-pegasus"]  # noqa: E501
        if instrument not in allowed_values:
            raise ValueError(
                "Invalid value for `instrument` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument, allowed_values)
            )

        self._instrument = instrument

    @property
    def refuge(self):
        """Gets the refuge of this Crosswalk.  # noqa: E501

        Does the crosswalk have a central island pedestrian refuge  # noqa: E501

        :return: The refuge of this Crosswalk.  # noqa: E501
        :rtype: bool
        """
        return self._refuge

    @refuge.setter
    def refuge(self, refuge):
        """Sets the refuge of this Crosswalk.

        Does the crosswalk have a central island pedestrian refuge  # noqa: E501

        :param refuge: The refuge of this Crosswalk.  # noqa: E501
        :type: bool
        """

        self._refuge = refuge

    @property
    def beacon(self):
        """Gets the beacon of this Crosswalk.  # noqa: E501

        The beacon type used for this crosswalk  # noqa: E501

        :return: The beacon of this Crosswalk.  # noqa: E501
        :rtype: str
        """
        return self._beacon

    @beacon.setter
    def beacon(self, beacon):
        """Sets the beacon of this Crosswalk.

        The beacon type used for this crosswalk  # noqa: E501

        :param beacon: The beacon of this Crosswalk.  # noqa: E501
        :type: str
        """
        allowed_values = ["phb", "belisha", "signal", "rapid-flash"]  # noqa: E501
        if beacon not in allowed_values:
            raise ValueError(
                "Invalid value for `beacon` ({0}), must be one of {1}"  # noqa: E501
                .format(beacon, allowed_values)
            )

        self._beacon = beacon

    @property
    def phases(self):
        """Gets the phases of this Crosswalk.  # noqa: E501

        A list of valid phases for the crosswalk if equipped with a graphical display  # noqa: E501

        :return: The phases of this Crosswalk.  # noqa: E501
        :rtype: list[str]
        """
        return self._phases

    @phases.setter
    def phases(self, phases):
        """Sets the phases of this Crosswalk.

        A list of valid phases for the crosswalk if equipped with a graphical display  # noqa: E501

        :param phases: The phases of this Crosswalk.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["walk-text", "do-not-walk-text", "steady-upraised-hand", "steady-walking-man", "flashing-upraised-hand"]  # noqa: E501
        if not set(phases).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `phases` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(phases) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._phases = phases

    @property
    def countdown(self):
        """Gets the countdown of this Crosswalk.  # noqa: E501

        Does the crosswalk feature an instrumented phase timer  # noqa: E501

        :return: The countdown of this Crosswalk.  # noqa: E501
        :rtype: bool
        """
        return self._countdown

    @countdown.setter
    def countdown(self, countdown):
        """Sets the countdown of this Crosswalk.

        Does the crosswalk feature an instrumented phase timer  # noqa: E501

        :param countdown: The countdown of this Crosswalk.  # noqa: E501
        :type: bool
        """

        self._countdown = countdown

    @property
    def audible(self):
        """Gets the audible of this Crosswalk.  # noqa: E501

        Is the crosswalk equipped with an audible warning for the crossing/countdown  # noqa: E501

        :return: The audible of this Crosswalk.  # noqa: E501
        :rtype: bool
        """
        return self._audible

    @audible.setter
    def audible(self, audible):
        """Sets the audible of this Crosswalk.

        Is the crosswalk equipped with an audible warning for the crossing/countdown  # noqa: E501

        :param audible: The audible of this Crosswalk.  # noqa: E501
        :type: bool
        """

        self._audible = audible

    @property
    def visor(self):
        """Gets the visor of this Crosswalk.  # noqa: E501

        The type of visor installed on the beacon  # noqa: E501

        :return: The visor of this Crosswalk.  # noqa: E501
        :rtype: str
        """
        return self._visor

    @visor.setter
    def visor(self, visor):
        """Sets the visor of this Crosswalk.

        The type of visor installed on the beacon  # noqa: E501

        :param visor: The visor of this Crosswalk.  # noqa: E501
        :type: str
        """
        allowed_values = ["egg-crate", "tunnel", "cap"]  # noqa: E501
        if visor not in allowed_values:
            raise ValueError(
                "Invalid value for `visor` ({0}), must be one of {1}"  # noqa: E501
                .format(visor, allowed_values)
            )

        self._visor = visor

    @property
    def call_button(self):
        """Gets the call_button of this Crosswalk.  # noqa: E501

        Can a pedestrian place a call or trigger this crosswalk with a button  # noqa: E501

        :return: The call_button of this Crosswalk.  # noqa: E501
        :rtype: bool
        """
        return self._call_button

    @call_button.setter
    def call_button(self, call_button):
        """Sets the call_button of this Crosswalk.

        Can a pedestrian place a call or trigger this crosswalk with a button  # noqa: E501

        :param call_button: The call_button of this Crosswalk.  # noqa: E501
        :type: bool
        """

        self._call_button = call_button

    @property
    def tactile_surface(self):
        """Gets the tactile_surface of this Crosswalk.  # noqa: E501

        Does the entrance to the crosswalk feature a tactile surface  # noqa: E501

        :return: The tactile_surface of this Crosswalk.  # noqa: E501
        :rtype: bool
        """
        return self._tactile_surface

    @tactile_surface.setter
    def tactile_surface(self, tactile_surface):
        """Sets the tactile_surface of this Crosswalk.

        Does the entrance to the crosswalk feature a tactile surface  # noqa: E501

        :param tactile_surface: The tactile_surface of this Crosswalk.  # noqa: E501
        :type: bool
        """

        self._tactile_surface = tactile_surface

    @property
    def state(self):
        """Gets the state of this Crosswalk.  # noqa: E501


        :return: The state of this Crosswalk.  # noqa: E501
        :rtype: CrosswalkState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Crosswalk.


        :param state: The state of this Crosswalk.  # noqa: E501
        :type: CrosswalkState
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
        if issubclass(Crosswalk, dict):
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
        if not isinstance(other, Crosswalk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
