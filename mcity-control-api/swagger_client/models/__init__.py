# coding: utf-8

# flake8: noqa
"""
    Mcity Control API

    Mcity implementation of OCTANE RESTful/Websocket API designed for autonomous and connected vehicle test facilities/cities.  # noqa: E501

    OpenAPI spec version: 0.0.10
    Contact: mcity-engineering@umich.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.api_error import APIError
from swagger_client.models.arrow_board import ArrowBoard
from swagger_client.models.body import Body
from swagger_client.models.body1 import Body1
from swagger_client.models.body10 import Body10
from swagger_client.models.body11 import Body11
from swagger_client.models.body12 import Body12
from swagger_client.models.body13 import Body13
from swagger_client.models.body14 import Body14
from swagger_client.models.body15 import Body15
from swagger_client.models.body16 import Body16
from swagger_client.models.body17 import Body17
from swagger_client.models.body18 import Body18
from swagger_client.models.body19 import Body19
from swagger_client.models.body2 import Body2
from swagger_client.models.body20 import Body20
from swagger_client.models.body21 import Body21
from swagger_client.models.body22 import Body22
from swagger_client.models.body23 import Body23
from swagger_client.models.body24 import Body24
from swagger_client.models.body25 import Body25
from swagger_client.models.body26 import Body26
from swagger_client.models.body27 import Body27
from swagger_client.models.body28 import Body28
from swagger_client.models.body29 import Body29
from swagger_client.models.body3 import Body3
from swagger_client.models.body30 import Body30
from swagger_client.models.body31 import Body31
from swagger_client.models.body32 import Body32
from swagger_client.models.body33 import Body33
from swagger_client.models.body34 import Body34
from swagger_client.models.body35 import Body35
from swagger_client.models.body36 import Body36
from swagger_client.models.body37 import Body37
from swagger_client.models.body38 import Body38
from swagger_client.models.body39 import Body39
from swagger_client.models.body4 import Body4
from swagger_client.models.body40 import Body40
from swagger_client.models.body41 import Body41
from swagger_client.models.body42 import Body42
from swagger_client.models.body5 import Body5
from swagger_client.models.body6 import Body6
from swagger_client.models.body7 import Body7
from swagger_client.models.body8 import Body8
from swagger_client.models.body9 import Body9
from swagger_client.models.crosswalk import Crosswalk
from swagger_client.models.crosswalk_state import CrosswalkState
from swagger_client.models.crosswalkid_state import CrosswalkidState
from swagger_client.models.facility import Facility
from swagger_client.models.facility_contact import FacilityContact
from swagger_client.models.facility_lr import FacilityLr
from swagger_client.models.facility_message import FacilityMessage
from swagger_client.models.facility_overlays import FacilityOverlays
from swagger_client.models.facility_ul import FacilityUl
from swagger_client.models.favorite import Favorite
from swagger_client.models.garage import Garage
from swagger_client.models.garage_state import GarageState
from swagger_client.models.garageid_state import GarageidState
from swagger_client.models.gate import Gate
from swagger_client.models.gate_state import GateState
from swagger_client.models.gateid_state import GateidState
from swagger_client.models.ipc_message import IPCMessage
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response20010 import InlineResponse20010
from swagger_client.models.inline_response20011 import InlineResponse20011
from swagger_client.models.inline_response20012 import InlineResponse20012
from swagger_client.models.inline_response20013 import InlineResponse20013
from swagger_client.models.inline_response20014 import InlineResponse20014
from swagger_client.models.inline_response20015 import InlineResponse20015
from swagger_client.models.inline_response20016 import InlineResponse20016
from swagger_client.models.inline_response20017 import InlineResponse20017
from swagger_client.models.inline_response20018 import InlineResponse20018
from swagger_client.models.inline_response20019 import InlineResponse20019
from swagger_client.models.inline_response2002 import InlineResponse2002
from swagger_client.models.inline_response20020 import InlineResponse20020
from swagger_client.models.inline_response20021 import InlineResponse20021
from swagger_client.models.inline_response20022 import InlineResponse20022
from swagger_client.models.inline_response20023 import InlineResponse20023
from swagger_client.models.inline_response20024 import InlineResponse20024
from swagger_client.models.inline_response20025 import InlineResponse20025
from swagger_client.models.inline_response20026 import InlineResponse20026
from swagger_client.models.inline_response20027 import InlineResponse20027
from swagger_client.models.inline_response20028 import InlineResponse20028
from swagger_client.models.inline_response20029 import InlineResponse20029
from swagger_client.models.inline_response2003 import InlineResponse2003
from swagger_client.models.inline_response20030 import InlineResponse20030
from swagger_client.models.inline_response20031 import InlineResponse20031
from swagger_client.models.inline_response20032 import InlineResponse20032
from swagger_client.models.inline_response20033 import InlineResponse20033
from swagger_client.models.inline_response20034 import InlineResponse20034
from swagger_client.models.inline_response20035 import InlineResponse20035
from swagger_client.models.inline_response20036 import InlineResponse20036
from swagger_client.models.inline_response20037 import InlineResponse20037
from swagger_client.models.inline_response20038 import InlineResponse20038
from swagger_client.models.inline_response20039 import InlineResponse20039
from swagger_client.models.inline_response2004 import InlineResponse2004
from swagger_client.models.inline_response20040 import InlineResponse20040
from swagger_client.models.inline_response20041 import InlineResponse20041
from swagger_client.models.inline_response20042 import InlineResponse20042
from swagger_client.models.inline_response20043 import InlineResponse20043
from swagger_client.models.inline_response20044 import InlineResponse20044
from swagger_client.models.inline_response20045 import InlineResponse20045
from swagger_client.models.inline_response20046 import InlineResponse20046
from swagger_client.models.inline_response20047 import InlineResponse20047
from swagger_client.models.inline_response20048 import InlineResponse20048
from swagger_client.models.inline_response20049 import InlineResponse20049
from swagger_client.models.inline_response2005 import InlineResponse2005
from swagger_client.models.inline_response20050 import InlineResponse20050
from swagger_client.models.inline_response20051 import InlineResponse20051
from swagger_client.models.inline_response20052 import InlineResponse20052
from swagger_client.models.inline_response20053 import InlineResponse20053
from swagger_client.models.inline_response20054 import InlineResponse20054
from swagger_client.models.inline_response20055 import InlineResponse20055
from swagger_client.models.inline_response20056 import InlineResponse20056
from swagger_client.models.inline_response20057 import InlineResponse20057
from swagger_client.models.inline_response20057_sessions import InlineResponse20057Sessions
from swagger_client.models.inline_response20058 import InlineResponse20058
from swagger_client.models.inline_response20058_session import InlineResponse20058Session
from swagger_client.models.inline_response20059 import InlineResponse20059
from swagger_client.models.inline_response2006 import InlineResponse2006
from swagger_client.models.inline_response20060 import InlineResponse20060
from swagger_client.models.inline_response20061 import InlineResponse20061
from swagger_client.models.inline_response20062 import InlineResponse20062
from swagger_client.models.inline_response20063 import InlineResponse20063
from swagger_client.models.inline_response20064 import InlineResponse20064
from swagger_client.models.inline_response20065 import InlineResponse20065
from swagger_client.models.inline_response2007 import InlineResponse2007
from swagger_client.models.inline_response2008 import InlineResponse2008
from swagger_client.models.inline_response2009 import InlineResponse2009
from swagger_client.models.intersection import Intersection
from swagger_client.models.intersection_stages import IntersectionStages
from swagger_client.models.intersection_state import IntersectionState
from swagger_client.models.intersection_state_phases import IntersectionStatePhases
from swagger_client.models.intersectionid_state import IntersectionidState
from swagger_client.models.intersectionidpreemptpreempt_id_state import IntersectionidpreemptpreemptIdState
from swagger_client.models.intersections_state import IntersectionsState
from swagger_client.models.lawn_mower import LawnMower
from swagger_client.models.lawn_mower_state import LawnMowerState
from swagger_client.models.light import Light
from swagger_client.models.light_state import LightState
from swagger_client.models.lightid_state import LightidState
from swagger_client.models.lights_state import LightsState
from swagger_client.models.maintenance_equipment import MaintenanceEquipment
from swagger_client.models.maintenancelawnmowerid_state import MaintenancelawnmoweridState
from swagger_client.models.managementfacilityreset_state import ManagementfacilityresetState
from swagger_client.models.managementpollingintersections_state import ManagementpollingintersectionsState
from swagger_client.models.message_board import MessageBoard
from swagger_client.models.one_of_maintenance_equipment_state import OneOfMaintenanceEquipmentState
from swagger_client.models.phase import Phase
from swagger_client.models.phase_stop_bar import PhaseStopBar
from swagger_client.models.phase_stop_bar_ll import PhaseStopBarLl
from swagger_client.models.phase_stop_bar_lr import PhaseStopBarLr
from swagger_client.models.phase_stop_bar_ul import PhaseStopBarUl
from swagger_client.models.phase_stop_bar_ur import PhaseStopBarUr
from swagger_client.models.railcrossing import Railcrossing
from swagger_client.models.railcrossing_state import RailcrossingState
from swagger_client.models.railcrossingid_state import RailcrossingidState
from swagger_client.models.safety_equipment import SafetyEquipment
from swagger_client.models.safetyarrowboardid_state import SafetyarrowboardidState
from swagger_client.models.safetymessageboardid_state import SafetymessageboardidState
from swagger_client.models.scenario import Scenario
from swagger_client.models.scenarioid_scenario import ScenarioidScenario
from swagger_client.models.sensor import Sensor
from swagger_client.models.sensor_camera import SensorCamera
from swagger_client.models.sensor_lidar import SensorLIDAR
from swagger_client.models.sensor_package import SensorPackage
from swagger_client.models.sensor_radar import SensorRADAR
from swagger_client.models.sensor_state import SensorState
from swagger_client.models.sensors_state import SensorsState
from swagger_client.models.sign_board_state import SignBoardState
from swagger_client.models.signal import Signal
from swagger_client.models.signal_state import SignalState
from swagger_client.models.signal_state_left import SignalStateLeft
from swagger_client.models.signal_state_right import SignalStateRight
from swagger_client.models.signal_state_straight import SignalStateStraight
from swagger_client.models.signalid_state import SignalidState
from swagger_client.models.signalid_state_left import SignalidStateLeft
from swagger_client.models.stage import Stage
from swagger_client.models.user_message import UserMessage
from swagger_client.models.v2_x import V2X
from swagger_client.models.v2_xbsm import V2XBSM
from swagger_client.models.v2_xpsm import V2XPSM
from swagger_client.models.v2_x_radios_supported import V2XRadiosSupported
from swagger_client.models.v2_x_raw import V2XRaw
from swagger_client.models.v2_xs_pa_t import V2XSPaT
from swagger_client.models.v2_xs_pa_t_phases import V2XSPaTPhases
from swagger_client.models.v2_x_state import V2XState
from swagger_client.models.v2_x_state_radios_enabled import V2XStateRadiosEnabled
from swagger_client.models.v2xobuid_state import V2xobuidState
from swagger_client.models.v2xrsus_state import V2xrsusState
from swagger_client.models.weather_alert import WeatherAlert
from swagger_client.models.weather_alert_state import WeatherAlertState
