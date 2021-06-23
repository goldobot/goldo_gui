# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/nucleo/robot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from goldo import pb2_options_pb2 as goldo_dot_pb2__options__pb2
from goldo import rplidar_pb2 as goldo_dot_rplidar__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/nucleo/robot.proto',
  package='goldo.nucleo.robot',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18goldo/nucleo/robot.proto\x12\x12goldo.nucleo.robot\x1a\x17goldo/pb2_options.proto\x1a\x13goldo/rplidar.proto\x1a\x1egoogle/protobuf/wrappers.proto\"%\n\x0f\x43onfigLoadBegin\x12\x12\n\x04size\x18\x01 \x01(\rB\x04\x80\xb5\x18\x05\"\x1f\n\x0f\x43onfigLoadChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\"\n\rConfigLoadEnd\x12\x11\n\x03\x63rc\x18\x01 \x01(\rB\x04\x80\xb5\x18\x05\"v\n\x10\x43onfigLoadStatus\x12\x41\n\x06status\x18\x01 \x01(\x0e\x32+.goldo.nucleo.robot.ConfigLoadStatus.StatusB\x04\x80\xb5\x18\x03\"\x1f\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\r\n\tCRC_ERROR\x10\x01\"\xca\x01\n\x0bServoConfig\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32\x1d.goldo.nucleo.robot.ServoTypeB\x04\x80\xb5\x18\x03\x12\x10\n\x02id\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x16\n\x08\x63w_limit\x18\x03 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tccw_limit\x18\x04 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tmax_speed\x18\x05 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x18\n\nmax_torque\x18\x06 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x12\n\x04name\x18@ \x01(\tB\x04\x80\xb5\x18\x0c\"?\n\x0cServosConfig\x12/\n\x06servos\x18\x01 \x03(\x0b\x32\x1f.goldo.nucleo.robot.ServoConfig\"R\n\rRPLidarConfig\x12\x14\n\x0ctheta_offset\x18\x01 \x01(\x02\x12+\n\ttresholds\x18\x02 \x01(\x0b\x32\x18.goldo.rplidar.Tresholds*N\n\tServoType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x12\n\x0e\x44YNAMIXEL_AX12\x10\x02\x12\x12\n\x0e\x44YNAMIXEL_MX28\x10\x03\x62\x06proto3')
  ,
  dependencies=[goldo_dot_pb2__options__pb2.DESCRIPTOR,goldo_dot_rplidar__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])

_SERVOTYPE = _descriptor.EnumDescriptor(
  name='ServoType',
  full_name='goldo.nucleo.robot.ServoType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STANDARD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIXEL_AX12', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIXEL_MX28', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=708,
  serialized_end=786,
)
_sym_db.RegisterEnumDescriptor(_SERVOTYPE)

ServoType = enum_type_wrapper.EnumTypeWrapper(_SERVOTYPE)
UNKNOWN = 0
STANDARD = 1
DYNAMIXEL_AX12 = 2
DYNAMIXEL_MX28 = 3


_CONFIGLOADSTATUS_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='goldo.nucleo.robot.ConfigLoadStatus.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRC_ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=321,
  serialized_end=352,
)
_sym_db.RegisterEnumDescriptor(_CONFIGLOADSTATUS_STATUS)


_CONFIGLOADBEGIN = _descriptor.Descriptor(
  name='ConfigLoadBegin',
  full_name='goldo.nucleo.robot.ConfigLoadBegin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='goldo.nucleo.robot.ConfigLoadBegin.size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
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
  serialized_start=126,
  serialized_end=163,
)


_CONFIGLOADCHUNK = _descriptor.Descriptor(
  name='ConfigLoadChunk',
  full_name='goldo.nucleo.robot.ConfigLoadChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='goldo.nucleo.robot.ConfigLoadChunk.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=165,
  serialized_end=196,
)


_CONFIGLOADEND = _descriptor.Descriptor(
  name='ConfigLoadEnd',
  full_name='goldo.nucleo.robot.ConfigLoadEnd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='crc', full_name='goldo.nucleo.robot.ConfigLoadEnd.crc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
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
  serialized_start=198,
  serialized_end=232,
)


_CONFIGLOADSTATUS = _descriptor.Descriptor(
  name='ConfigLoadStatus',
  full_name='goldo.nucleo.robot.ConfigLoadStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='goldo.nucleo.robot.ConfigLoadStatus.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIGLOADSTATUS_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=352,
)


_SERVOCONFIG = _descriptor.Descriptor(
  name='ServoConfig',
  full_name='goldo.nucleo.robot.ServoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='goldo.nucleo.robot.ServoConfig.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='goldo.nucleo.robot.ServoConfig.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cw_limit', full_name='goldo.nucleo.robot.ServoConfig.cw_limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ccw_limit', full_name='goldo.nucleo.robot.ServoConfig.ccw_limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_speed', full_name='goldo.nucleo.robot.ServoConfig.max_speed', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_torque', full_name='goldo.nucleo.robot.ServoConfig.max_torque', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='goldo.nucleo.robot.ServoConfig.name', index=6,
      number=64, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\014'), file=DESCRIPTOR),
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
  serialized_start=355,
  serialized_end=557,
)


_SERVOSCONFIG = _descriptor.Descriptor(
  name='ServosConfig',
  full_name='goldo.nucleo.robot.ServosConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servos', full_name='goldo.nucleo.robot.ServosConfig.servos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=559,
  serialized_end=622,
)


_RPLIDARCONFIG = _descriptor.Descriptor(
  name='RPLidarConfig',
  full_name='goldo.nucleo.robot.RPLidarConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='theta_offset', full_name='goldo.nucleo.robot.RPLidarConfig.theta_offset', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tresholds', full_name='goldo.nucleo.robot.RPLidarConfig.tresholds', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=624,
  serialized_end=706,
)

_CONFIGLOADSTATUS.fields_by_name['status'].enum_type = _CONFIGLOADSTATUS_STATUS
_CONFIGLOADSTATUS_STATUS.containing_type = _CONFIGLOADSTATUS
_SERVOCONFIG.fields_by_name['type'].enum_type = _SERVOTYPE
_SERVOSCONFIG.fields_by_name['servos'].message_type = _SERVOCONFIG
_RPLIDARCONFIG.fields_by_name['tresholds'].message_type = goldo_dot_rplidar__pb2._TRESHOLDS
DESCRIPTOR.message_types_by_name['ConfigLoadBegin'] = _CONFIGLOADBEGIN
DESCRIPTOR.message_types_by_name['ConfigLoadChunk'] = _CONFIGLOADCHUNK
DESCRIPTOR.message_types_by_name['ConfigLoadEnd'] = _CONFIGLOADEND
DESCRIPTOR.message_types_by_name['ConfigLoadStatus'] = _CONFIGLOADSTATUS
DESCRIPTOR.message_types_by_name['ServoConfig'] = _SERVOCONFIG
DESCRIPTOR.message_types_by_name['ServosConfig'] = _SERVOSCONFIG
DESCRIPTOR.message_types_by_name['RPLidarConfig'] = _RPLIDARCONFIG
DESCRIPTOR.enum_types_by_name['ServoType'] = _SERVOTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigLoadBegin = _reflection.GeneratedProtocolMessageType('ConfigLoadBegin', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGLOADBEGIN,
  __module__ = 'goldo.nucleo.robot_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.robot.ConfigLoadBegin)
  ))
_sym_db.RegisterMessage(ConfigLoadBegin)

ConfigLoadChunk = _reflection.GeneratedProtocolMessageType('ConfigLoadChunk', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGLOADCHUNK,
  __module__ = 'goldo.nucleo.robot_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.robot.ConfigLoadChunk)
  ))
_sym_db.RegisterMessage(ConfigLoadChunk)

ConfigLoadEnd = _reflection.GeneratedProtocolMessageType('ConfigLoadEnd', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGLOADEND,
  __module__ = 'goldo.nucleo.robot_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.robot.ConfigLoadEnd)
  ))
_sym_db.RegisterMessage(ConfigLoadEnd)

ConfigLoadStatus = _reflection.GeneratedProtocolMessageType('ConfigLoadStatus', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGLOADSTATUS,
  __module__ = 'goldo.nucleo.robot_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.robot.ConfigLoadStatus)
  ))
_sym_db.RegisterMessage(ConfigLoadStatus)

ServoConfig = _reflection.GeneratedProtocolMessageType('ServoConfig', (_message.Message,), dict(
  DESCRIPTOR = _SERVOCONFIG,
  __module__ = 'goldo.nucleo.robot_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.robot.ServoConfig)
  ))
_sym_db.RegisterMessage(ServoConfig)

ServosConfig = _reflection.GeneratedProtocolMessageType('ServosConfig', (_message.Message,), dict(
  DESCRIPTOR = _SERVOSCONFIG,
  __module__ = 'goldo.nucleo.robot_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.robot.ServosConfig)
  ))
_sym_db.RegisterMessage(ServosConfig)

RPLidarConfig = _reflection.GeneratedProtocolMessageType('RPLidarConfig', (_message.Message,), dict(
  DESCRIPTOR = _RPLIDARCONFIG,
  __module__ = 'goldo.nucleo.robot_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.robot.RPLidarConfig)
  ))
_sym_db.RegisterMessage(RPLidarConfig)


_CONFIGLOADBEGIN.fields_by_name['size']._options = None
_CONFIGLOADEND.fields_by_name['crc']._options = None
_CONFIGLOADSTATUS.fields_by_name['status']._options = None
_SERVOCONFIG.fields_by_name['type']._options = None
_SERVOCONFIG.fields_by_name['id']._options = None
_SERVOCONFIG.fields_by_name['cw_limit']._options = None
_SERVOCONFIG.fields_by_name['ccw_limit']._options = None
_SERVOCONFIG.fields_by_name['max_speed']._options = None
_SERVOCONFIG.fields_by_name['max_torque']._options = None
_SERVOCONFIG.fields_by_name['name']._options = None
# @@protoc_insertion_point(module_scope)
