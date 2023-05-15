# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/strategy.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from goldo.common import geometry_pb2 as goldo_dot_common_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/strategy.proto',
  package='goldo.strategy',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14goldo/strategy.proto\x12\x0egoldo.strategy\x1a\x1bgoldo/common/geometry.proto\"\xae\x01\n\x04\x41rea\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x03\x62ox\x18\x02 \x01(\x0b\x32\x1a.goldo.common.geometry.BoxH\x00\x12/\n\x06\x63ircle\x18\x03 \x01(\x0b\x32\x1d.goldo.common.geometry.CircleH\x00\x12\x30\n\x06polygo\x18\x04 \x01(\x0b\x32\x1e.goldo.common.geometry.PolygonH\x00\x42\n\n\x08geometry\"\xec\x01\n\x0c\x41\x63tionConfig\x12\x35\n\nstart_pose\x18\x01 \x01(\x0b\x32!.goldo.common.geometry.StaticPose\x12\x17\n\x0fsequence_action\x18\x02 \x01(\t\x12\x18\n\x10sequence_prepare\x18\x03 \x01(\t\x12\x1e\n\x16sequence_prepare_abort\x18\x04 \x01(\t\x12\x1b\n\x13sequence_on_success\x18\x05 \x01(\t\x12\x1b\n\x13sequence_on_failure\x18\x06 \x01(\t\x12\x18\n\x10\x64\x65\x66\x61ult_priority\x18\x07 \x01(\x05\"\xc1\x01\n\x0eStrategyConfig\x12<\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32+.goldo.strategy.StrategyConfig.ActionsEntry\x12#\n\x05\x61reas\x18\x02 \x03(\x0b\x32\x14.goldo.strategy.Area\x1aL\n\x0c\x41\x63tionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.goldo.strategy.ActionConfig:\x02\x38\x01\"\x0f\n\rStrategyStateb\x06proto3'
  ,
  dependencies=[goldo_dot_common_dot_geometry__pb2.DESCRIPTOR,])




_AREA = _descriptor.Descriptor(
  name='Area',
  full_name='goldo.strategy.Area',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='goldo.strategy.Area.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='box', full_name='goldo.strategy.Area.box', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='circle', full_name='goldo.strategy.Area.circle', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='polygo', full_name='goldo.strategy.Area.polygo', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='geometry', full_name='goldo.strategy.Area.geometry',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=70,
  serialized_end=244,
)


_ACTIONCONFIG = _descriptor.Descriptor(
  name='ActionConfig',
  full_name='goldo.strategy.ActionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_pose', full_name='goldo.strategy.ActionConfig.start_pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_action', full_name='goldo.strategy.ActionConfig.sequence_action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_prepare', full_name='goldo.strategy.ActionConfig.sequence_prepare', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_prepare_abort', full_name='goldo.strategy.ActionConfig.sequence_prepare_abort', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_on_success', full_name='goldo.strategy.ActionConfig.sequence_on_success', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_on_failure', full_name='goldo.strategy.ActionConfig.sequence_on_failure', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_priority', full_name='goldo.strategy.ActionConfig.default_priority', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=247,
  serialized_end=483,
)


_STRATEGYCONFIG_ACTIONSENTRY = _descriptor.Descriptor(
  name='ActionsEntry',
  full_name='goldo.strategy.StrategyConfig.ActionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='goldo.strategy.StrategyConfig.ActionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='goldo.strategy.StrategyConfig.ActionsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=603,
  serialized_end=679,
)

_STRATEGYCONFIG = _descriptor.Descriptor(
  name='StrategyConfig',
  full_name='goldo.strategy.StrategyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actions', full_name='goldo.strategy.StrategyConfig.actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='areas', full_name='goldo.strategy.StrategyConfig.areas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STRATEGYCONFIG_ACTIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=679,
)


_STRATEGYSTATE = _descriptor.Descriptor(
  name='StrategyState',
  full_name='goldo.strategy.StrategyState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=681,
  serialized_end=696,
)

_AREA.fields_by_name['box'].message_type = goldo_dot_common_dot_geometry__pb2._BOX
_AREA.fields_by_name['circle'].message_type = goldo_dot_common_dot_geometry__pb2._CIRCLE
_AREA.fields_by_name['polygo'].message_type = goldo_dot_common_dot_geometry__pb2._POLYGON
_AREA.oneofs_by_name['geometry'].fields.append(
  _AREA.fields_by_name['box'])
_AREA.fields_by_name['box'].containing_oneof = _AREA.oneofs_by_name['geometry']
_AREA.oneofs_by_name['geometry'].fields.append(
  _AREA.fields_by_name['circle'])
_AREA.fields_by_name['circle'].containing_oneof = _AREA.oneofs_by_name['geometry']
_AREA.oneofs_by_name['geometry'].fields.append(
  _AREA.fields_by_name['polygo'])
_AREA.fields_by_name['polygo'].containing_oneof = _AREA.oneofs_by_name['geometry']
_ACTIONCONFIG.fields_by_name['start_pose'].message_type = goldo_dot_common_dot_geometry__pb2._STATICPOSE
_STRATEGYCONFIG_ACTIONSENTRY.fields_by_name['value'].message_type = _ACTIONCONFIG
_STRATEGYCONFIG_ACTIONSENTRY.containing_type = _STRATEGYCONFIG
_STRATEGYCONFIG.fields_by_name['actions'].message_type = _STRATEGYCONFIG_ACTIONSENTRY
_STRATEGYCONFIG.fields_by_name['areas'].message_type = _AREA
DESCRIPTOR.message_types_by_name['Area'] = _AREA
DESCRIPTOR.message_types_by_name['ActionConfig'] = _ACTIONCONFIG
DESCRIPTOR.message_types_by_name['StrategyConfig'] = _STRATEGYCONFIG
DESCRIPTOR.message_types_by_name['StrategyState'] = _STRATEGYSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Area = _reflection.GeneratedProtocolMessageType('Area', (_message.Message,), {
  'DESCRIPTOR' : _AREA,
  '__module__' : 'goldo.strategy_pb2'
  # @@protoc_insertion_point(class_scope:goldo.strategy.Area)
  })
_sym_db.RegisterMessage(Area)

ActionConfig = _reflection.GeneratedProtocolMessageType('ActionConfig', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONCONFIG,
  '__module__' : 'goldo.strategy_pb2'
  # @@protoc_insertion_point(class_scope:goldo.strategy.ActionConfig)
  })
_sym_db.RegisterMessage(ActionConfig)

StrategyConfig = _reflection.GeneratedProtocolMessageType('StrategyConfig', (_message.Message,), {

  'ActionsEntry' : _reflection.GeneratedProtocolMessageType('ActionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _STRATEGYCONFIG_ACTIONSENTRY,
    '__module__' : 'goldo.strategy_pb2'
    # @@protoc_insertion_point(class_scope:goldo.strategy.StrategyConfig.ActionsEntry)
    })
  ,
  'DESCRIPTOR' : _STRATEGYCONFIG,
  '__module__' : 'goldo.strategy_pb2'
  # @@protoc_insertion_point(class_scope:goldo.strategy.StrategyConfig)
  })
_sym_db.RegisterMessage(StrategyConfig)
_sym_db.RegisterMessage(StrategyConfig.ActionsEntry)

StrategyState = _reflection.GeneratedProtocolMessageType('StrategyState', (_message.Message,), {
  'DESCRIPTOR' : _STRATEGYSTATE,
  '__module__' : 'goldo.strategy_pb2'
  # @@protoc_insertion_point(class_scope:goldo.strategy.StrategyState)
  })
_sym_db.RegisterMessage(StrategyState)


_STRATEGYCONFIG_ACTIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
