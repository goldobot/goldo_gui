# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/strategy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
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
  serialized_pb=_b('\n\x14goldo/strategy.proto\x12\x0egoldo.strategy\x1a\x1bgoldo/common/geometry.proto\")\n\x04Pose\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\x0b\n\x03yaw\x18\x03 \x01(\x02\"\xb5\x01\n\x0c\x41\x63tionConfig\x12(\n\nstart_pose\x18\x01 \x01(\x0b\x32\x14.goldo.strategy.Pose\x12\x17\n\x0fsequence_action\x18\x02 \x01(\t\x12\x18\n\x10sequence_prepare\x18\x03 \x01(\t\x12\x1f\n\x17sequence_prepare_cancel\x18\x04 \x01(\t\x12\x15\n\rsequence_post\x18\x05 \x01(\t\x12\x10\n\x08priority\x18\x06 \x01(\x05\"\x9c\x01\n\x0eStrategyConfig\x12<\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32+.goldo.strategy.StrategyConfig.ActionsEntry\x1aL\n\x0c\x41\x63tionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.goldo.strategy.ActionConfig:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[goldo_dot_common_dot_geometry__pb2.DESCRIPTOR,])




_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='goldo.strategy.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='goldo.strategy.Pose.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='goldo.strategy.Pose.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='goldo.strategy.Pose.yaw', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=69,
  serialized_end=110,
)


_ACTIONCONFIG = _descriptor.Descriptor(
  name='ActionConfig',
  full_name='goldo.strategy.ActionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_pose', full_name='goldo.strategy.ActionConfig.start_pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_action', full_name='goldo.strategy.ActionConfig.sequence_action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_prepare', full_name='goldo.strategy.ActionConfig.sequence_prepare', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_prepare_cancel', full_name='goldo.strategy.ActionConfig.sequence_prepare_cancel', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_post', full_name='goldo.strategy.ActionConfig.sequence_post', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priority', full_name='goldo.strategy.ActionConfig.priority', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=113,
  serialized_end=294,
)


_STRATEGYCONFIG_ACTIONSENTRY = _descriptor.Descriptor(
  name='ActionsEntry',
  full_name='goldo.strategy.StrategyConfig.ActionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='goldo.strategy.StrategyConfig.ActionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='goldo.strategy.StrategyConfig.ActionsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=377,
  serialized_end=453,
)

_STRATEGYCONFIG = _descriptor.Descriptor(
  name='StrategyConfig',
  full_name='goldo.strategy.StrategyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actions', full_name='goldo.strategy.StrategyConfig.actions', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=297,
  serialized_end=453,
)

_ACTIONCONFIG.fields_by_name['start_pose'].message_type = _POSE
_STRATEGYCONFIG_ACTIONSENTRY.fields_by_name['value'].message_type = _ACTIONCONFIG
_STRATEGYCONFIG_ACTIONSENTRY.containing_type = _STRATEGYCONFIG
_STRATEGYCONFIG.fields_by_name['actions'].message_type = _STRATEGYCONFIG_ACTIONSENTRY
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
DESCRIPTOR.message_types_by_name['ActionConfig'] = _ACTIONCONFIG
DESCRIPTOR.message_types_by_name['StrategyConfig'] = _STRATEGYCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), dict(
  DESCRIPTOR = _POSE,
  __module__ = 'goldo.strategy_pb2'
  # @@protoc_insertion_point(class_scope:goldo.strategy.Pose)
  ))
_sym_db.RegisterMessage(Pose)

ActionConfig = _reflection.GeneratedProtocolMessageType('ActionConfig', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONCONFIG,
  __module__ = 'goldo.strategy_pb2'
  # @@protoc_insertion_point(class_scope:goldo.strategy.ActionConfig)
  ))
_sym_db.RegisterMessage(ActionConfig)

StrategyConfig = _reflection.GeneratedProtocolMessageType('StrategyConfig', (_message.Message,), dict(

  ActionsEntry = _reflection.GeneratedProtocolMessageType('ActionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _STRATEGYCONFIG_ACTIONSENTRY,
    __module__ = 'goldo.strategy_pb2'
    # @@protoc_insertion_point(class_scope:goldo.strategy.StrategyConfig.ActionsEntry)
    ))
  ,
  DESCRIPTOR = _STRATEGYCONFIG,
  __module__ = 'goldo.strategy_pb2'
  # @@protoc_insertion_point(class_scope:goldo.strategy.StrategyConfig)
  ))
_sym_db.RegisterMessage(StrategyConfig)
_sym_db.RegisterMessage(StrategyConfig.ActionsEntry)


_STRATEGYCONFIG_ACTIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
