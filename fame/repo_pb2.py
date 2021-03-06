# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: repo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='repo.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nrepo.proto\":\n\x06\x43ommit\x12\x0b\n\x03sha\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\"2\n\tCommitter\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x13\n\x0bnum_commits\x18\x02 \x01(\x05\"\xcf\x02\n\x04Repo\x12\r\n\x05owner\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12$\n\x10top_contributors\x18\x04 \x03(\x0b\x32\n.Committer\x12\x1f\n\x0erecent_commits\x18\x05 \x03(\x0b\x32\x07.Commit\x12\x18\n\x10new_contributors\x18\x06 \x03(\t\x12#\n\x07\x61vatars\x18\x07 \x03(\x0b\x32\x12.Repo.AvatarsEntry\x12\x1c\n\x06status\x18\x08 \x01(\x0e\x32\x0c.Repo.Status\x12\x15\n\rerror_message\x18\t \x01(\t\x1a.\n\x0c\x41vatarsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x06Status\x12\x0f\n\x0bUNPROCESSED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x62\x06proto3')
)



_REPO_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='Repo.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNPROCESSED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=413,
  serialized_end=462,
)
_sym_db.RegisterEnumDescriptor(_REPO_STATUS)


_COMMIT = _descriptor.Descriptor(
  name='Commit',
  full_name='Commit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sha', full_name='Commit.sha', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Commit.timestamp', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='Commit.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=72,
)


_COMMITTER = _descriptor.Descriptor(
  name='Committer',
  full_name='Committer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='Committer.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_commits', full_name='Committer.num_commits', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=124,
)


_REPO_AVATARSENTRY = _descriptor.Descriptor(
  name='AvatarsEntry',
  full_name='Repo.AvatarsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Repo.AvatarsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Repo.AvatarsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=411,
)

_REPO = _descriptor.Descriptor(
  name='Repo',
  full_name='Repo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='Repo.owner', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Repo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='Repo.user', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_contributors', full_name='Repo.top_contributors', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recent_commits', full_name='Repo.recent_commits', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_contributors', full_name='Repo.new_contributors', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatars', full_name='Repo.avatars', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='Repo.status', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='Repo.error_message', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REPO_AVATARSENTRY, ],
  enum_types=[
    _REPO_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=462,
)

_REPO_AVATARSENTRY.containing_type = _REPO
_REPO.fields_by_name['top_contributors'].message_type = _COMMITTER
_REPO.fields_by_name['recent_commits'].message_type = _COMMIT
_REPO.fields_by_name['avatars'].message_type = _REPO_AVATARSENTRY
_REPO.fields_by_name['status'].enum_type = _REPO_STATUS
_REPO_STATUS.containing_type = _REPO
DESCRIPTOR.message_types_by_name['Commit'] = _COMMIT
DESCRIPTOR.message_types_by_name['Committer'] = _COMMITTER
DESCRIPTOR.message_types_by_name['Repo'] = _REPO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Commit = _reflection.GeneratedProtocolMessageType('Commit', (_message.Message,), dict(
  DESCRIPTOR = _COMMIT,
  __module__ = 'repo_pb2'
  # @@protoc_insertion_point(class_scope:Commit)
  ))
_sym_db.RegisterMessage(Commit)

Committer = _reflection.GeneratedProtocolMessageType('Committer', (_message.Message,), dict(
  DESCRIPTOR = _COMMITTER,
  __module__ = 'repo_pb2'
  # @@protoc_insertion_point(class_scope:Committer)
  ))
_sym_db.RegisterMessage(Committer)

Repo = _reflection.GeneratedProtocolMessageType('Repo', (_message.Message,), dict(

  AvatarsEntry = _reflection.GeneratedProtocolMessageType('AvatarsEntry', (_message.Message,), dict(
    DESCRIPTOR = _REPO_AVATARSENTRY,
    __module__ = 'repo_pb2'
    # @@protoc_insertion_point(class_scope:Repo.AvatarsEntry)
    ))
  ,
  DESCRIPTOR = _REPO,
  __module__ = 'repo_pb2'
  # @@protoc_insertion_point(class_scope:Repo)
  ))
_sym_db.RegisterMessage(Repo)
_sym_db.RegisterMessage(Repo.AvatarsEntry)


_REPO_AVATARSENTRY.has_options = True
_REPO_AVATARSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
