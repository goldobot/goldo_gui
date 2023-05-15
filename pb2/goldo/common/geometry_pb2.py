# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: goldo/common/geometry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='goldo/common/geometry.proto',
  package='goldo.common.geometry',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bgoldo/common/geometry.proto\x12\x15goldo.common.geometry\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\".\n\nPointCloud\x12\x12\n\nnum_points\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"I\n\nStaticPose\x12.\n\x08position\x18\x01 \x01(\x0b\x32\x1c.goldo.common.geometry.Point\x12\x0b\n\x03yaw\x18\x02 \x01(\x02\"\x98\x01\n\x04Pose\x12.\n\x08position\x18\x01 \x01(\x0b\x32\x1c.goldo.common.geometry.Point\x12\x0b\n\x03yaw\x18\x02 \x01(\x02\x12\r\n\x05speed\x18\x03 \x01(\x02\x12\x10\n\x08yaw_rate\x18\x04 \x01(\x02\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x05 \x01(\x02\x12\x1c\n\x14\x61ngular_acceleration\x18\x06 \x01(\x02\"F\n\x06\x43ircle\x12,\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x1c.goldo.common.geometry.Point\x12\x0e\n\x06radius\x18\x02 \x01(\x02\"]\n\x03\x42ox\x12*\n\x04pmin\x18\x01 \x01(\x0b\x32\x1c.goldo.common.geometry.Point\x12*\n\x04pmax\x18\x02 \x01(\x0b\x32\x1c.goldo.common.geometry.Point\"9\n\x07Polygon\x12.\n\x08vertices\x18\x01 \x03(\x0b\x32\x1c.goldo.common.geometry.Pointb\x06proto3'
)




_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='goldo.common.geometry.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='goldo.common.geometry.Point.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='goldo.common.geometry.Point.y', index=1,
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
  serialized_start=54,
  serialized_end=83,
)


_POINTCLOUD = _descriptor.Descriptor(
  name='PointCloud',
  full_name='goldo.common.geometry.PointCloud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_points', full_name='goldo.common.geometry.PointCloud.num_points', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='goldo.common.geometry.PointCloud.data', index=1,
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
  serialized_start=85,
  serialized_end=131,
)


_STATICPOSE = _descriptor.Descriptor(
  name='StaticPose',
  full_name='goldo.common.geometry.StaticPose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='goldo.common.geometry.StaticPose.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='goldo.common.geometry.StaticPose.yaw', index=1,
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
  serialized_start=133,
  serialized_end=206,
)


_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='goldo.common.geometry.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='goldo.common.geometry.Pose.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='goldo.common.geometry.Pose.yaw', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='goldo.common.geometry.Pose.speed', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw_rate', full_name='goldo.common.geometry.Pose.yaw_rate', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='goldo.common.geometry.Pose.acceleration', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angular_acceleration', full_name='goldo.common.geometry.Pose.angular_acceleration', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  serialized_start=209,
  serialized_end=361,
)


_CIRCLE = _descriptor.Descriptor(
  name='Circle',
  full_name='goldo.common.geometry.Circle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='center', full_name='goldo.common.geometry.Circle.center', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='radius', full_name='goldo.common.geometry.Circle.radius', index=1,
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
  serialized_start=363,
  serialized_end=433,
)


_BOX = _descriptor.Descriptor(
  name='Box',
  full_name='goldo.common.geometry.Box',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pmin', full_name='goldo.common.geometry.Box.pmin', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pmax', full_name='goldo.common.geometry.Box.pmax', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=528,
)


_POLYGON = _descriptor.Descriptor(
  name='Polygon',
  full_name='goldo.common.geometry.Polygon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertices', full_name='goldo.common.geometry.Polygon.vertices', index=0,
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
  serialized_start=530,
  serialized_end=587,
)

_STATICPOSE.fields_by_name['position'].message_type = _POINT
_POSE.fields_by_name['position'].message_type = _POINT
_CIRCLE.fields_by_name['center'].message_type = _POINT
_BOX.fields_by_name['pmin'].message_type = _POINT
_BOX.fields_by_name['pmax'].message_type = _POINT
_POLYGON.fields_by_name['vertices'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['PointCloud'] = _POINTCLOUD
DESCRIPTOR.message_types_by_name['StaticPose'] = _STATICPOSE
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
DESCRIPTOR.message_types_by_name['Circle'] = _CIRCLE
DESCRIPTOR.message_types_by_name['Box'] = _BOX
DESCRIPTOR.message_types_by_name['Polygon'] = _POLYGON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'goldo.common.geometry_pb2'
  # @@protoc_insertion_point(class_scope:goldo.common.geometry.Point)
  })
_sym_db.RegisterMessage(Point)

PointCloud = _reflection.GeneratedProtocolMessageType('PointCloud', (_message.Message,), {
  'DESCRIPTOR' : _POINTCLOUD,
  '__module__' : 'goldo.common.geometry_pb2'
  # @@protoc_insertion_point(class_scope:goldo.common.geometry.PointCloud)
  })
_sym_db.RegisterMessage(PointCloud)

StaticPose = _reflection.GeneratedProtocolMessageType('StaticPose', (_message.Message,), {
  'DESCRIPTOR' : _STATICPOSE,
  '__module__' : 'goldo.common.geometry_pb2'
  # @@protoc_insertion_point(class_scope:goldo.common.geometry.StaticPose)
  })
_sym_db.RegisterMessage(StaticPose)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), {
  'DESCRIPTOR' : _POSE,
  '__module__' : 'goldo.common.geometry_pb2'
  # @@protoc_insertion_point(class_scope:goldo.common.geometry.Pose)
  })
_sym_db.RegisterMessage(Pose)

Circle = _reflection.GeneratedProtocolMessageType('Circle', (_message.Message,), {
  'DESCRIPTOR' : _CIRCLE,
  '__module__' : 'goldo.common.geometry_pb2'
  # @@protoc_insertion_point(class_scope:goldo.common.geometry.Circle)
  })
_sym_db.RegisterMessage(Circle)

Box = _reflection.GeneratedProtocolMessageType('Box', (_message.Message,), {
  'DESCRIPTOR' : _BOX,
  '__module__' : 'goldo.common.geometry_pb2'
  # @@protoc_insertion_point(class_scope:goldo.common.geometry.Box)
  })
_sym_db.RegisterMessage(Box)

Polygon = _reflection.GeneratedProtocolMessageType('Polygon', (_message.Message,), {
  'DESCRIPTOR' : _POLYGON,
  '__module__' : 'goldo.common.geometry_pb2'
  # @@protoc_insertion_point(class_scope:goldo.common.geometry.Polygon)
  })
_sym_db.RegisterMessage(Polygon)


# @@protoc_insertion_point(module_scope)
