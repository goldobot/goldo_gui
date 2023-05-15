# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/nucleo/fpga.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from goldo import pb2_options_pb2 as goldo_dot_pb2__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/nucleo/fpga.proto',
  package='goldo.nucleo.fpga',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17goldo/nucleo/fpga.proto\x12\x11goldo.nucleo.fpga\x1a\x17goldo/pb2_options.proto\"$\n\x07RegRead\x12\x19\n\x0b\x61pb_address\x18\x01 \x01(\x07\x42\x04\x80\xb5\x18\x07\"C\n\rRegReadStatus\x12\x19\n\x0b\x61pb_address\x18\x01 \x01(\x07\x42\x04\x80\xb5\x18\x07\x12\x17\n\tapb_value\x18\x02 \x01(\x07\x42\x04\x80\xb5\x18\x07\">\n\x08RegWrite\x12\x19\n\x0b\x61pb_address\x18\x01 \x01(\x07\x42\x04\x80\xb5\x18\x07\x12\x17\n\tapb_value\x18\x02 \x01(\x07\x42\x04\x80\xb5\x18\x07\"\x1d\n\x07\x41\x64\x63Read\x12\x12\n\x04\x63han\x18\x01 \x01(\x07\x42\x04\x80\xb5\x18\x07\"2\n\nAdcReadOut\x12\x12\n\x04\x63han\x18\x01 \x01(\x07\x42\x04\x80\xb5\x18\x07\x12\x10\n\x08\x63han_val\x18\x02 \x01(\x02\x62\x06proto3'
  ,
  dependencies=[goldo_dot_pb2__options__pb2.DESCRIPTOR,])




_REGREAD = _descriptor.Descriptor(
  name='RegRead',
  full_name='goldo.nucleo.fpga.RegRead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='apb_address', full_name='goldo.nucleo.fpga.RegRead.apb_address', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=71,
  serialized_end=107,
)


_REGREADSTATUS = _descriptor.Descriptor(
  name='RegReadStatus',
  full_name='goldo.nucleo.fpga.RegReadStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='apb_address', full_name='goldo.nucleo.fpga.RegReadStatus.apb_address', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='apb_value', full_name='goldo.nucleo.fpga.RegReadStatus.apb_value', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=109,
  serialized_end=176,
)


_REGWRITE = _descriptor.Descriptor(
  name='RegWrite',
  full_name='goldo.nucleo.fpga.RegWrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='apb_address', full_name='goldo.nucleo.fpga.RegWrite.apb_address', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='apb_value', full_name='goldo.nucleo.fpga.RegWrite.apb_value', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=178,
  serialized_end=240,
)


_ADCREAD = _descriptor.Descriptor(
  name='AdcRead',
  full_name='goldo.nucleo.fpga.AdcRead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chan', full_name='goldo.nucleo.fpga.AdcRead.chan', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=242,
  serialized_end=271,
)


_ADCREADOUT = _descriptor.Descriptor(
  name='AdcReadOut',
  full_name='goldo.nucleo.fpga.AdcReadOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chan', full_name='goldo.nucleo.fpga.AdcReadOut.chan', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\200\265\030\007', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chan_val', full_name='goldo.nucleo.fpga.AdcReadOut.chan_val', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=273,
  serialized_end=323,
)

DESCRIPTOR.message_types_by_name['RegRead'] = _REGREAD
DESCRIPTOR.message_types_by_name['RegReadStatus'] = _REGREADSTATUS
DESCRIPTOR.message_types_by_name['RegWrite'] = _REGWRITE
DESCRIPTOR.message_types_by_name['AdcRead'] = _ADCREAD
DESCRIPTOR.message_types_by_name['AdcReadOut'] = _ADCREADOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegRead = _reflection.GeneratedProtocolMessageType('RegRead', (_message.Message,), {
  'DESCRIPTOR' : _REGREAD,
  '__module__' : 'goldo.nucleo.fpga_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.fpga.RegRead)
  })
_sym_db.RegisterMessage(RegRead)

RegReadStatus = _reflection.GeneratedProtocolMessageType('RegReadStatus', (_message.Message,), {
  'DESCRIPTOR' : _REGREADSTATUS,
  '__module__' : 'goldo.nucleo.fpga_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.fpga.RegReadStatus)
  })
_sym_db.RegisterMessage(RegReadStatus)

RegWrite = _reflection.GeneratedProtocolMessageType('RegWrite', (_message.Message,), {
  'DESCRIPTOR' : _REGWRITE,
  '__module__' : 'goldo.nucleo.fpga_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.fpga.RegWrite)
  })
_sym_db.RegisterMessage(RegWrite)

AdcRead = _reflection.GeneratedProtocolMessageType('AdcRead', (_message.Message,), {
  'DESCRIPTOR' : _ADCREAD,
  '__module__' : 'goldo.nucleo.fpga_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.fpga.AdcRead)
  })
_sym_db.RegisterMessage(AdcRead)

AdcReadOut = _reflection.GeneratedProtocolMessageType('AdcReadOut', (_message.Message,), {
  'DESCRIPTOR' : _ADCREADOUT,
  '__module__' : 'goldo.nucleo.fpga_pb2'
  # @@protoc_insertion_point(class_scope:goldo.nucleo.fpga.AdcReadOut)
  })
_sym_db.RegisterMessage(AdcReadOut)


_REGREAD.fields_by_name['apb_address']._options = None
_REGREADSTATUS.fields_by_name['apb_address']._options = None
_REGREADSTATUS.fields_by_name['apb_value']._options = None
_REGWRITE.fields_by_name['apb_address']._options = None
_REGWRITE.fields_by_name['apb_value']._options = None
_ADCREAD.fields_by_name['chan']._options = None
_ADCREADOUT.fields_by_name['chan']._options = None
# @@protoc_insertion_point(module_scope)
