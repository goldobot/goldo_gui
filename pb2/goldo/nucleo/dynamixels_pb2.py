# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/nucleo/dynamixels.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from goldo import pb2_options_pb2 as goldo_dot_pb2__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/nucleo/dynamixels.proto',
  package='goldo.nucleo.dynamixels',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dgoldo/nucleo/dynamixels.proto\x12\x17goldo.nucleo.dynamixels\x1a\x17goldo/pb2_options.proto\"\x83\x03\n\rRequestPacket\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\rB\x04\x80\xb5\x18\x05\x12\x1e\n\x10protocol_version\x18\x02 \x01(\rB\x04\x80\xb5\x18\x03\x12\x10\n\x02id\x18\x03 \x01(\rB\x04\x80\xb5\x18\x03\x12\x45\n\x07\x63ommand\x18\x04 \x01(\x0e\x32..goldo.nucleo.dynamixels.RequestPacket.CommandB\x04\x80\xb5\x18\x03\x12\x0f\n\x07payload\x18\x05 \x01(\x0c\"\xc8\x01\n\x07\x43ommand\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04PING\x10\x01\x12\x08\n\x04READ\x10\x02\x12\t\n\x05WRITE\x10\x03\x12\r\n\tREG_WRITE\x10\x04\x12\n\n\x06\x41\x43TION\x10\x05\x12\x11\n\rFACTORY_RESET\x10\x06\x12\n\n\x06REBOOT\x10\x08\x12\t\n\x05\x43LEAR\x10\x10\x12\n\n\x06STATUS\x10U\x12\x0e\n\tSYNC_READ\x10\x82\x01\x12\x0f\n\nSYNC_WRITE\x10\x83\x01\x12\x0e\n\tBULK_READ\x10\x92\x01\x12\x0f\n\nBULK_WRITE\x10\x93\x01\"\x8d\x01\n\x0eResponsePacket\x12\x1d\n\x0fsequence_number\x18\x01 \x01(\rB\x04\x80\xb5\x18\x05\x12\x1e\n\x10protocol_version\x18\x02 \x01(\rB\x04\x80\xb5\x18\x03\x12\x10\n\x02id\x18\x03 \x01(\rB\x04\x80\xb5\x18\x03\x12\x19\n\x0b\x65rror_flags\x18\x04 \x01(\rB\x04\x80\xb5\x18\x03\x12\x0f\n\x07payload\x18\x05 \x01(\x0c\x62\x06proto3'
  ,
  dependencies=[goldo_dot_pb2__options__pb2.DESCRIPTOR,])



_REQUESTPACKET_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='goldo.nucleo.dynamixels.RequestPacket.Command',
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
      name='PING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='READ', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REG_WRITE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FACTORY_RESET', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REBOOT', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLEAR', index=8, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=9, number=85,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SYNC_READ', index=10, number=130,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SYNC_WRITE', index=11, number=131,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BULK_READ', index=12, number=146,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BULK_WRITE', index=13, number=147,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=271,
  serialized_end=471,
)
_sym_db.RegisterEnumDescriptor(_REQUESTPACKET_COMMAND)


_REQUESTPACKET = _descriptor.Descriptor(
  name='RequestPacket',
  full_name='goldo.nucleo.dynamixels.RequestPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='goldo.nucleo.dynamixels.RequestPacket.sequence_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='goldo.nucleo.dynamixels.RequestPacket.protocol_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='goldo.nucleo.dynamixels.RequestPacket.id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command', full_name='goldo.nucleo.dynamixels.RequestPacket.command', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='goldo.nucleo.dynamixels.RequestPacket.payload', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTPACKET_COMMAND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=471,
)


_RESPONSEPACKET = _descriptor.Descriptor(
  name='ResponsePacket',
  full_name='goldo.nucleo.dynamixels.ResponsePacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='goldo.nucleo.dynamixels.ResponsePacket.sequence_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='goldo.nucleo.dynamixels.ResponsePacket.protocol_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='goldo.nucleo.dynamixels.ResponsePacket.id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_flags', full_name='goldo.nucleo.dynamixels.ResponsePacket.error_flags', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='goldo.nucleo.dynamixels.ResponsePacket.payload', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=474,
  serialized_end=615,
)

_REQUESTPACKET.fields_by_name['command'].enum_type = _REQUESTPACKET_COMMAND
_REQUESTPACKET_COMMAND.containing_type = _REQUESTPACKET
DESCRIPTOR.message_types_by_name['RequestPacket'] = _REQUESTPACKET
DESCRIPTOR.message_types_by_name['ResponsePacket'] = _RESPONSEPACKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestPacket = _reflection.GeneratedProtocolMessageType('RequestPacket', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTPACKET,
  '__module__' : 'goldo.nucleo.dynamixels_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.dynamixels.RequestPacket)
  })
_sym_db.RegisterMessage(RequestPacket)

ResponsePacket = _reflection.GeneratedProtocolMessageType('ResponsePacket', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEPACKET,
  '__module__' : 'goldo.nucleo.dynamixels_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.dynamixels.ResponsePacket)
  })
_sym_db.RegisterMessage(ResponsePacket)


_REQUESTPACKET.fields_by_name['sequence_number']._options = None
_REQUESTPACKET.fields_by_name['protocol_version']._options = None
_REQUESTPACKET.fields_by_name['id']._options = None
_REQUESTPACKET.fields_by_name['command']._options = None
_RESPONSEPACKET.fields_by_name['sequence_number']._options = None
_RESPONSEPACKET.fields_by_name['protocol_version']._options = None
_RESPONSEPACKET.fields_by_name['id']._options = None
_RESPONSEPACKET.fields_by_name['error_flags']._options = None
# @@protoc_insertion_point(module_scope)
