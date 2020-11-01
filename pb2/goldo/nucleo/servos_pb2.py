# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/nucleo/servos.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from goldo import pb2_options_pb2 as goldo_dot_pb2__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/nucleo/servos.proto',
  package='goldo.nucleo.servos',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19goldo/nucleo/servos.proto\x12\x13goldo.nucleo.servos\x1a\x17goldo/pb2_options.proto\"\xcb\x01\n\x0bServoConfig\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32\x1e.goldo.nucleo.servos.ServoTypeB\x04\x80\xb5\x18\x03\x12\x10\n\x02id\x18\x02 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x16\n\x08\x63w_limit\x18\x03 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tccw_limit\x18\x04 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x17\n\tmax_speed\x18\x05 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x18\n\nmax_torque\x18\x06 \x01(\x05\x42\x04\x80\xb5\x18\x05\x12\x12\n\x04name\x18@ \x01(\tB\x04\x80\xb5\x18\x0c\"@\n\x0cServosConfig\x12\x30\n\x06servos\x18\x01 \x03(\x0b\x32 .goldo.nucleo.servos.ServoConfig\"K\n\x04Move\x12\x16\n\x08servo_id\x18\x01 \x01(\x05\x42\x04\x80\xb5\x18\x03\x12\x16\n\x08position\x18\x02 \x01(\rB\x04\x80\xb5\x18\x05\x12\x13\n\x05speed\x18\x03 \x01(\rB\x04\x80\xb5\x18\x05*N\n\tServoType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x12\n\x0e\x44YNAMIXEL_AX12\x10\x02\x12\x12\n\x0e\x44YNAMIXEL_MX28\x10\x03\x62\x06proto3'
  ,
  dependencies=[goldo_dot_pb2__options__pb2.DESCRIPTOR,])

_SERVOTYPE = _descriptor.EnumDescriptor(
  name='ServoType',
  full_name='goldo.nucleo.servos.ServoType',
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
      name='STANDARD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIXEL_AX12', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIXEL_MX28', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=424,
  serialized_end=502,
)
_sym_db.RegisterEnumDescriptor(_SERVOTYPE)

ServoType = enum_type_wrapper.EnumTypeWrapper(_SERVOTYPE)
UNKNOWN = 0
STANDARD = 1
DYNAMIXEL_AX12 = 2
DYNAMIXEL_MX28 = 3



_SERVOCONFIG = _descriptor.Descriptor(
  name='ServoConfig',
  full_name='goldo.nucleo.servos.ServoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='goldo.nucleo.servos.ServoConfig.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='goldo.nucleo.servos.ServoConfig.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cw_limit', full_name='goldo.nucleo.servos.ServoConfig.cw_limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ccw_limit', full_name='goldo.nucleo.servos.ServoConfig.ccw_limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_speed', full_name='goldo.nucleo.servos.ServoConfig.max_speed', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_torque', full_name='goldo.nucleo.servos.ServoConfig.max_torque', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='goldo.nucleo.servos.ServoConfig.name', index=6,
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
  serialized_start=76,
  serialized_end=279,
)


_SERVOSCONFIG = _descriptor.Descriptor(
  name='ServosConfig',
  full_name='goldo.nucleo.servos.ServosConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='servos', full_name='goldo.nucleo.servos.ServosConfig.servos', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=281,
  serialized_end=345,
)


_MOVE = _descriptor.Descriptor(
  name='Move',
  full_name='goldo.nucleo.servos.Move',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='servo_id', full_name='goldo.nucleo.servos.Move.servo_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='position', full_name='goldo.nucleo.servos.Move.position', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='goldo.nucleo.servos.Move.speed', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=347,
  serialized_end=422,
)

_SERVOCONFIG.fields_by_name['type'].enum_type = _SERVOTYPE
_SERVOSCONFIG.fields_by_name['servos'].message_type = _SERVOCONFIG
DESCRIPTOR.message_types_by_name['ServoConfig'] = _SERVOCONFIG
DESCRIPTOR.message_types_by_name['ServosConfig'] = _SERVOSCONFIG
DESCRIPTOR.message_types_by_name['Move'] = _MOVE
DESCRIPTOR.enum_types_by_name['ServoType'] = _SERVOTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServoConfig = _reflection.GeneratedProtocolMessageType('ServoConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVOCONFIG,
  '__module__' : 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.ServoConfig)
  })
_sym_db.RegisterMessage(ServoConfig)

ServosConfig = _reflection.GeneratedProtocolMessageType('ServosConfig', (_message.Message,), {
  'DESCRIPTOR' : _SERVOSCONFIG,
  '__module__' : 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.ServosConfig)
  })
_sym_db.RegisterMessage(ServosConfig)

Move = _reflection.GeneratedProtocolMessageType('Move', (_message.Message,), {
  'DESCRIPTOR' : _MOVE,
  '__module__' : 'goldo.nucleo.servos_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.servos.Move)
  })
_sym_db.RegisterMessage(Move)


_SERVOCONFIG.fields_by_name['type']._options = None
_SERVOCONFIG.fields_by_name['id']._options = None
_SERVOCONFIG.fields_by_name['cw_limit']._options = None
_SERVOCONFIG.fields_by_name['ccw_limit']._options = None
_SERVOCONFIG.fields_by_name['max_speed']._options = None
_SERVOCONFIG.fields_by_name['max_torque']._options = None
_SERVOCONFIG.fields_by_name['name']._options = None
_MOVE.fields_by_name['servo_id']._options = None
_MOVE.fields_by_name['position']._options = None
_MOVE.fields_by_name['speed']._options = None
# @@protoc_insertion_point(module_scope)