# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/nucleo.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from goldo.nucleo import hal_pb2 as goldo_dot_nucleo_dot_hal__pb2
from goldo.nucleo import odometry_pb2 as goldo_dot_nucleo_dot_odometry__pb2
from goldo.nucleo import propulsion_pb2 as goldo_dot_nucleo_dot_propulsion__pb2
from goldo.nucleo import robot_simulator_pb2 as goldo_dot_nucleo_dot_robot__simulator__pb2
from goldo.nucleo import servos_pb2 as goldo_dot_nucleo_dot_servos__pb2
from goldo.nucleo import odrive_pb2 as goldo_dot_nucleo_dot_odrive__pb2
from goldo.nucleo import statistics_pb2 as goldo_dot_nucleo_dot_statistics__pb2
from goldo import pb2_options_pb2 as goldo_dot_pb2__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/nucleo.proto',
  package='goldo.nucleo',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12goldo/nucleo.proto\x12\x0cgoldo.nucleo\x1a\x16goldo/nucleo/hal.proto\x1a\x1bgoldo/nucleo/odometry.proto\x1a\x1dgoldo/nucleo/propulsion.proto\x1a\"goldo/nucleo/robot_simulator.proto\x1a\x19goldo/nucleo/servos.proto\x1a\x19goldo/nucleo/odrive.proto\x1a\x1dgoldo/nucleo/statistics.proto\x1a\x17goldo/pb2_options.proto\"b\n\x0cSensorConfig\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x18.goldo.nucleo.SensorTypeB\x04\x80\xb5\x18\x03\x12\x10\n\x02id\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x12\n\x04name\x18@ \x01(\tB\x04\x80\xb5\x18\x0c\"\xf5\x03\n\x0cNucleoConfig\x12(\n\x03hal\x18\x01 \x01(\x0b\x32\x1b.goldo.nucleo.hal.HalConfig\x12K\n\x0frobot_simulator\x18\x02 \x01(\x0b\x32\x32.goldo.nucleo.robot_simulator.RobotSimulatorConfig\x12\x37\n\x08odometry\x18\x03 \x01(\x0b\x32%.goldo.nucleo.odometry.OdometryConfig\x12G\n\npropulsion\x18\x04 \x01(\x0b\x32\x33.goldo.nucleo.propulsion.PropulsionControllerConfig\x12\x46\n\x0fpropulsion_task\x18\x05 \x01(\x0b\x32-.goldo.nucleo.propulsion.PropulsionTaskConfig\x12\x30\n\x06servos\x18\x06 \x03(\x0b\x32 .goldo.nucleo.servos.ServoConfig\x12+\n\x07sensors\x18\x07 \x03(\x0b\x32\x1a.goldo.nucleo.SensorConfig\x12\x15\n\renabled_tasks\x18\x08 \x03(\t\x12.\n\x05lifts\x18\t \x03(\x0b\x32\x1f.goldo.nucleo.servos.LiftConfig\"%\n\x10NucleoTasksState\x12\x11\n\tcomm_uart\x18\x01 \x01(\x08\"\xea\x01\n\x15NucleoTasksStatistics\x12\x42\n\tuart_comm\x18\x01 \x01(\x0b\x32/.goldo.nucleo.statistics.UARTCommTaskStatistics\x12\x46\n\x0bodrive_comm\x18\x02 \x01(\x0b\x32\x31.goldo.nucleo.statistics.ODriveCommTaskStatistics\x12\x45\n\npropulsion\x18\x03 \x01(\x0b\x32\x31.goldo.nucleo.statistics.PropulsionTaskStatistics\"T\n\x11\x46reeRTOSTaskStats\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12\x17\n\x0fruntime_counter\x18\x02 \x01(\r\x12\x13\n\x0btask_number\x18\x03 \x01(\r\"D\n\x12\x46reeRTOSTasksStats\x12.\n\x05tasks\x18\x02 \x03(\x0b\x32\x1f.goldo.nucleo.FreeRTOSTaskStats\"\x82\x02\n\x0bNucleoState\x12\x11\n\tconnected\x18\x01 \x01(\x08\x12\x12\n\nconfigured\x18\x02 \x01(\x08\x12\x11\n\theartbeat\x18\x03 \x01(\r\x12=\n\x10tasks_statistics\x18\x04 \x01(\x0b\x32#.goldo.nucleo.NucleoTasksStatistics\x12\x31\n\x06odrive\x18\x05 \x01(\x0b\x32!.goldo.nucleo.odrive.ODriveStatus\x12G\n\x18odrive_client_statistics\x18\x06 \x01(\x0b\x32%.goldo.nucleo.odrive.ClientStatistics\"\xcc\x01\n\x12ScopeChannelConfig\x12\x16\n\x08variable\x18\x01 \x01(\rB\x04\x80\xb5\x18\x05\x12\x16\n\x08\x65ncoding\x18\x02 \x01(\rB\x04\x80\xb5\x18\x05\x12\x11\n\tmin_value\x18\x03 \x01(\x02\x12\x11\n\tmax_value\x18\x04 \x01(\x02\"`\n\x08\x45ncoding\x12\x08\n\x04RAW8\x10\x00\x12\t\n\x05RAW16\x10\x01\x12\t\n\x05RAW32\x10\x02\x12\x0b\n\x07SCALED8\x10\x04\x12\x0c\n\x08SCALED16\x10\x05\x12\x0c\n\x08SCALED32\x10\x06\x12\x0b\n\x07\x46LOAT32\x10\x08\"a\n\x0bScopeConfig\x12\x14\n\x06period\x18\x01 \x01(\rB\x04\x80\xb5\x18\x05\x12<\n\x08\x63hannels\x18\x02 \x03(\x0b\x32 .goldo.nucleo.ScopeChannelConfigB\x08\x98\xb5\x18\x05\x88\xb5\x18\x08\"2\n\tScopeData\x12\x17\n\ttimestamp\x18\x01 \x01(\rB\x04\x80\xb5\x18\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"*\n\x12ScopeChannelValues\x12\x14\n\x0c\x66loat_values\x18\x01 \x03(\x02\"U\n\x0bScopeValues\x12\x12\n\ntimestamps\x18\x01 \x03(\x02\x12\x32\n\x08\x63hannels\x18\x02 \x03(\x0b\x32 .goldo.nucleo.ScopeChannelValues*/\n\nSensorType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06NUCLEO\x10\x01\x12\x08\n\x04\x46PGA\x10\x02\x62\x06proto3'
  ,
  dependencies=[goldo_dot_nucleo_dot_hal__pb2.DESCRIPTOR,goldo_dot_nucleo_dot_odometry__pb2.DESCRIPTOR,goldo_dot_nucleo_dot_propulsion__pb2.DESCRIPTOR,goldo_dot_nucleo_dot_robot__simulator__pb2.DESCRIPTOR,goldo_dot_nucleo_dot_servos__pb2.DESCRIPTOR,goldo_dot_nucleo_dot_odrive__pb2.DESCRIPTOR,goldo_dot_nucleo_dot_statistics__pb2.DESCRIPTOR,goldo_dot_pb2__options__pb2.DESCRIPTOR,])

_SENSORTYPE = _descriptor.EnumDescriptor(
  name='SensorType',
  full_name='goldo.nucleo.SensorType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NUCLEO', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FPGA', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2052,
  serialized_end=2099,
)
_sym_db.RegisterEnumDescriptor(_SENSORTYPE)

SensorType = enum_type_wrapper.EnumTypeWrapper(_SENSORTYPE)
UNKNOWN = 0
NUCLEO = 1
FPGA = 2


_SCOPECHANNELCONFIG_ENCODING = _descriptor.EnumDescriptor(
  name='Encoding',
  full_name='goldo.nucleo.ScopeChannelConfig.Encoding',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAW8', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RAW16', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RAW32', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALED8', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALED16', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCALED32', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLOAT32', index=6, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1672,
  serialized_end=1768,
)
_sym_db.RegisterEnumDescriptor(_SCOPECHANNELCONFIG_ENCODING)


_SENSORCONFIG = _descriptor.Descriptor(
  name='SensorConfig',
  full_name='goldo.nucleo.SensorConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='goldo.nucleo.SensorConfig.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='goldo.nucleo.SensorConfig.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='goldo.nucleo.SensorConfig.name', index=2,
      number=64, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\014', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=364,
)


_NUCLEOCONFIG = _descriptor.Descriptor(
  name='NucleoConfig',
  full_name='goldo.nucleo.NucleoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hal', full_name='goldo.nucleo.NucleoConfig.hal', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='robot_simulator', full_name='goldo.nucleo.NucleoConfig.robot_simulator', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='odometry', full_name='goldo.nucleo.NucleoConfig.odometry', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propulsion', full_name='goldo.nucleo.NucleoConfig.propulsion', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propulsion_task', full_name='goldo.nucleo.NucleoConfig.propulsion_task', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='servos', full_name='goldo.nucleo.NucleoConfig.servos', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sensors', full_name='goldo.nucleo.NucleoConfig.sensors', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled_tasks', full_name='goldo.nucleo.NucleoConfig.enabled_tasks', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lifts', full_name='goldo.nucleo.NucleoConfig.lifts', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=868,
)


_NUCLEOTASKSSTATE = _descriptor.Descriptor(
  name='NucleoTasksState',
  full_name='goldo.nucleo.NucleoTasksState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='comm_uart', full_name='goldo.nucleo.NucleoTasksState.comm_uart', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=870,
  serialized_end=907,
)


_NUCLEOTASKSSTATISTICS = _descriptor.Descriptor(
  name='NucleoTasksStatistics',
  full_name='goldo.nucleo.NucleoTasksStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uart_comm', full_name='goldo.nucleo.NucleoTasksStatistics.uart_comm', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='odrive_comm', full_name='goldo.nucleo.NucleoTasksStatistics.odrive_comm', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propulsion', full_name='goldo.nucleo.NucleoTasksStatistics.propulsion', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=910,
  serialized_end=1144,
)


_FREERTOSTASKSTATS = _descriptor.Descriptor(
  name='FreeRTOSTaskStats',
  full_name='goldo.nucleo.FreeRTOSTaskStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_name', full_name='goldo.nucleo.FreeRTOSTaskStats.task_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='runtime_counter', full_name='goldo.nucleo.FreeRTOSTaskStats.runtime_counter', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_number', full_name='goldo.nucleo.FreeRTOSTaskStats.task_number', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1146,
  serialized_end=1230,
)


_FREERTOSTASKSSTATS = _descriptor.Descriptor(
  name='FreeRTOSTasksStats',
  full_name='goldo.nucleo.FreeRTOSTasksStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='goldo.nucleo.FreeRTOSTasksStats.tasks', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1232,
  serialized_end=1300,
)


_NUCLEOSTATE = _descriptor.Descriptor(
  name='NucleoState',
  full_name='goldo.nucleo.NucleoState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connected', full_name='goldo.nucleo.NucleoState.connected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='configured', full_name='goldo.nucleo.NucleoState.configured', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heartbeat', full_name='goldo.nucleo.NucleoState.heartbeat', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tasks_statistics', full_name='goldo.nucleo.NucleoState.tasks_statistics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='odrive', full_name='goldo.nucleo.NucleoState.odrive', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='odrive_client_statistics', full_name='goldo.nucleo.NucleoState.odrive_client_statistics', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1303,
  serialized_end=1561,
)


_SCOPECHANNELCONFIG = _descriptor.Descriptor(
  name='ScopeChannelConfig',
  full_name='goldo.nucleo.ScopeChannelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable', full_name='goldo.nucleo.ScopeChannelConfig.variable', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='goldo.nucleo.ScopeChannelConfig.encoding', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_value', full_name='goldo.nucleo.ScopeChannelConfig.min_value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_value', full_name='goldo.nucleo.ScopeChannelConfig.max_value', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SCOPECHANNELCONFIG_ENCODING,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1564,
  serialized_end=1768,
)


_SCOPECONFIG = _descriptor.Descriptor(
  name='ScopeConfig',
  full_name='goldo.nucleo.ScopeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='period', full_name='goldo.nucleo.ScopeConfig.period', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='goldo.nucleo.ScopeConfig.channels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\230\265\030\005\210\265\030\010', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1770,
  serialized_end=1867,
)


_SCOPEDATA = _descriptor.Descriptor(
  name='ScopeData',
  full_name='goldo.nucleo.ScopeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='goldo.nucleo.ScopeData.timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='goldo.nucleo.ScopeData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1869,
  serialized_end=1919,
)


_SCOPECHANNELVALUES = _descriptor.Descriptor(
  name='ScopeChannelValues',
  full_name='goldo.nucleo.ScopeChannelValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='float_values', full_name='goldo.nucleo.ScopeChannelValues.float_values', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1921,
  serialized_end=1963,
)


_SCOPEVALUES = _descriptor.Descriptor(
  name='ScopeValues',
  full_name='goldo.nucleo.ScopeValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamps', full_name='goldo.nucleo.ScopeValues.timestamps', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channels', full_name='goldo.nucleo.ScopeValues.channels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1965,
  serialized_end=2050,
)

_SENSORCONFIG.fields_by_name['type'].enum_type = _SENSORTYPE
_NUCLEOCONFIG.fields_by_name['hal'].message_type = goldo_dot_nucleo_dot_hal__pb2._HALCONFIG
_NUCLEOCONFIG.fields_by_name['robot_simulator'].message_type = goldo_dot_nucleo_dot_robot__simulator__pb2._ROBOTSIMULATORCONFIG
_NUCLEOCONFIG.fields_by_name['odometry'].message_type = goldo_dot_nucleo_dot_odometry__pb2._ODOMETRYCONFIG
_NUCLEOCONFIG.fields_by_name['propulsion'].message_type = goldo_dot_nucleo_dot_propulsion__pb2._PROPULSIONCONTROLLERCONFIG
_NUCLEOCONFIG.fields_by_name['propulsion_task'].message_type = goldo_dot_nucleo_dot_propulsion__pb2._PROPULSIONTASKCONFIG
_NUCLEOCONFIG.fields_by_name['servos'].message_type = goldo_dot_nucleo_dot_servos__pb2._SERVOCONFIG
_NUCLEOCONFIG.fields_by_name['sensors'].message_type = _SENSORCONFIG
_NUCLEOCONFIG.fields_by_name['lifts'].message_type = goldo_dot_nucleo_dot_servos__pb2._LIFTCONFIG
_NUCLEOTASKSSTATISTICS.fields_by_name['uart_comm'].message_type = goldo_dot_nucleo_dot_statistics__pb2._UARTCOMMTASKSTATISTICS
_NUCLEOTASKSSTATISTICS.fields_by_name['odrive_comm'].message_type = goldo_dot_nucleo_dot_statistics__pb2._ODRIVECOMMTASKSTATISTICS
_NUCLEOTASKSSTATISTICS.fields_by_name['propulsion'].message_type = goldo_dot_nucleo_dot_statistics__pb2._PROPULSIONTASKSTATISTICS
_FREERTOSTASKSSTATS.fields_by_name['tasks'].message_type = _FREERTOSTASKSTATS
_NUCLEOSTATE.fields_by_name['tasks_statistics'].message_type = _NUCLEOTASKSSTATISTICS
_NUCLEOSTATE.fields_by_name['odrive'].message_type = goldo_dot_nucleo_dot_odrive__pb2._ODRIVESTATUS
_NUCLEOSTATE.fields_by_name['odrive_client_statistics'].message_type = goldo_dot_nucleo_dot_odrive__pb2._CLIENTSTATISTICS
_SCOPECHANNELCONFIG_ENCODING.containing_type = _SCOPECHANNELCONFIG
_SCOPECONFIG.fields_by_name['channels'].message_type = _SCOPECHANNELCONFIG
_SCOPEVALUES.fields_by_name['channels'].message_type = _SCOPECHANNELVALUES
DESCRIPTOR.message_types_by_name['SensorConfig'] = _SENSORCONFIG
DESCRIPTOR.message_types_by_name['NucleoConfig'] = _NUCLEOCONFIG
DESCRIPTOR.message_types_by_name['NucleoTasksState'] = _NUCLEOTASKSSTATE
DESCRIPTOR.message_types_by_name['NucleoTasksStatistics'] = _NUCLEOTASKSSTATISTICS
DESCRIPTOR.message_types_by_name['FreeRTOSTaskStats'] = _FREERTOSTASKSTATS
DESCRIPTOR.message_types_by_name['FreeRTOSTasksStats'] = _FREERTOSTASKSSTATS
DESCRIPTOR.message_types_by_name['NucleoState'] = _NUCLEOSTATE
DESCRIPTOR.message_types_by_name['ScopeChannelConfig'] = _SCOPECHANNELCONFIG
DESCRIPTOR.message_types_by_name['ScopeConfig'] = _SCOPECONFIG
DESCRIPTOR.message_types_by_name['ScopeData'] = _SCOPEDATA
DESCRIPTOR.message_types_by_name['ScopeChannelValues'] = _SCOPECHANNELVALUES
DESCRIPTOR.message_types_by_name['ScopeValues'] = _SCOPEVALUES
DESCRIPTOR.enum_types_by_name['SensorType'] = _SENSORTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SensorConfig = _reflection.GeneratedProtocolMessageType('SensorConfig', (_message.Message,), {
  'DESCRIPTOR' : _SENSORCONFIG,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.SensorConfig)
  })
_sym_db.RegisterMessage(SensorConfig)

NucleoConfig = _reflection.GeneratedProtocolMessageType('NucleoConfig', (_message.Message,), {
  'DESCRIPTOR' : _NUCLEOCONFIG,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.NucleoConfig)
  })
_sym_db.RegisterMessage(NucleoConfig)

NucleoTasksState = _reflection.GeneratedProtocolMessageType('NucleoTasksState', (_message.Message,), {
  'DESCRIPTOR' : _NUCLEOTASKSSTATE,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.NucleoTasksState)
  })
_sym_db.RegisterMessage(NucleoTasksState)

NucleoTasksStatistics = _reflection.GeneratedProtocolMessageType('NucleoTasksStatistics', (_message.Message,), {
  'DESCRIPTOR' : _NUCLEOTASKSSTATISTICS,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.NucleoTasksStatistics)
  })
_sym_db.RegisterMessage(NucleoTasksStatistics)

FreeRTOSTaskStats = _reflection.GeneratedProtocolMessageType('FreeRTOSTaskStats', (_message.Message,), {
  'DESCRIPTOR' : _FREERTOSTASKSTATS,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.FreeRTOSTaskStats)
  })
_sym_db.RegisterMessage(FreeRTOSTaskStats)

FreeRTOSTasksStats = _reflection.GeneratedProtocolMessageType('FreeRTOSTasksStats', (_message.Message,), {
  'DESCRIPTOR' : _FREERTOSTASKSSTATS,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.FreeRTOSTasksStats)
  })
_sym_db.RegisterMessage(FreeRTOSTasksStats)

NucleoState = _reflection.GeneratedProtocolMessageType('NucleoState', (_message.Message,), {
  'DESCRIPTOR' : _NUCLEOSTATE,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.NucleoState)
  })
_sym_db.RegisterMessage(NucleoState)

ScopeChannelConfig = _reflection.GeneratedProtocolMessageType('ScopeChannelConfig', (_message.Message,), {
  'DESCRIPTOR' : _SCOPECHANNELCONFIG,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.ScopeChannelConfig)
  })
_sym_db.RegisterMessage(ScopeChannelConfig)

ScopeConfig = _reflection.GeneratedProtocolMessageType('ScopeConfig', (_message.Message,), {
  'DESCRIPTOR' : _SCOPECONFIG,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.ScopeConfig)
  })
_sym_db.RegisterMessage(ScopeConfig)

ScopeData = _reflection.GeneratedProtocolMessageType('ScopeData', (_message.Message,), {
  'DESCRIPTOR' : _SCOPEDATA,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.ScopeData)
  })
_sym_db.RegisterMessage(ScopeData)

ScopeChannelValues = _reflection.GeneratedProtocolMessageType('ScopeChannelValues', (_message.Message,), {
  'DESCRIPTOR' : _SCOPECHANNELVALUES,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.ScopeChannelValues)
  })
_sym_db.RegisterMessage(ScopeChannelValues)

ScopeValues = _reflection.GeneratedProtocolMessageType('ScopeValues', (_message.Message,), {
  'DESCRIPTOR' : _SCOPEVALUES,
  '__module__' : 'goldo.nucleo_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.ScopeValues)
  })
_sym_db.RegisterMessage(ScopeValues)


_SENSORCONFIG.fields_by_name['type']._options = None
_SENSORCONFIG.fields_by_name['id']._options = None
_SENSORCONFIG.fields_by_name['name']._options = None
_SCOPECHANNELCONFIG.fields_by_name['variable']._options = None
_SCOPECHANNELCONFIG.fields_by_name['encoding']._options = None
_SCOPECONFIG.fields_by_name['period']._options = None
_SCOPECONFIG.fields_by_name['channels']._options = None
_SCOPEDATA.fields_by_name['timestamp']._options = None
# @@protoc_insertion_point(module_scope)
