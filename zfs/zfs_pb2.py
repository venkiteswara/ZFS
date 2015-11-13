# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zfs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='zfs.proto',
  package='zfs',
  syntax='proto3',
  serialized_pb=b'\n\tzfs.proto\x12\x03zfs\"\xb4\x01\n\x08\x46ileStat\x12\x0e\n\x06st_ino\x18\x01 \x01(\x05\x12\x0e\n\x06st_dev\x18\x02 \x01(\x05\x12\x0f\n\x07st_mode\x18\x03 \x01(\x05\x12\x10\n\x08st_nlink\x18\x04 \x01(\x05\x12\x0e\n\x06st_uid\x18\x05 \x01(\x05\x12\x0e\n\x06st_gid\x18\x06 \x01(\x05\x12\x0f\n\x07st_size\x18\x08 \x01(\x05\x12\x10\n\x08st_atime\x18\x0b \x01(\x02\x12\x10\n\x08st_mtime\x18\x0c \x01(\x02\x12\x10\n\x08st_ctime\x18\r \x01(\x02\"&\n\x08\x46ilePath\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\x05\"1\n\x08StdReply\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\"1\n\x0fTestAuthRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x10\n\x08st_mtime\x18\x02 \x01(\x02\"\x1d\n\rTestAuthReply\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x05\"#\n\rFileDataBlock\x12\x12\n\ndata_block\x18\x01 \x01(\t\"&\n\x0c\x44irListBlock\x12\x16\n\x0e\x64ir_list_block\x18\x01 \x01(\t\"%\n\tRenameMsg\x12\x0b\n\x03old\x18\x01 \x01(\t\x12\x0b\n\x03new\x18\x02 \x01(\t2\x8f\x04\n\x06ZfsRpc\x12-\n\x0bGetFileStat\x12\r.zfs.FilePath\x1a\r.zfs.FileStat\"\x00\x12\x36\n\x08TestAuth\x12\x14.zfs.TestAuthRequest\x1a\x12.zfs.TestAuthReply\"\x00\x12.\n\x05\x46\x65tch\x12\r.zfs.FilePath\x1a\x12.zfs.FileDataBlock\"\x00\x30\x01\x12.\n\x05Store\x12\x12.zfs.FileDataBlock\x1a\r.zfs.StdReply\"\x00(\x01\x12-\n\x0bSetFileStat\x12\r.zfs.FileStat\x1a\r.zfs.StdReply\"\x00\x12,\n\nRemoveFile\x12\r.zfs.FilePath\x1a\r.zfs.StdReply\"\x00\x12)\n\x07MakeDir\x12\r.zfs.FilePath\x1a\r.zfs.StdReply\"\x00\x12+\n\tRemoveDir\x12\r.zfs.FilePath\x1a\r.zfs.StdReply\"\x00\x12\x30\n\x08\x46\x65tchDir\x12\r.zfs.FilePath\x1a\x11.zfs.DirListBlock\"\x00\x30\x01\x12)\n\x06Rename\x12\x0e.zfs.RenameMsg\x1a\r.zfs.StdReply\"\x00\x12,\n\nCreateFile\x12\r.zfs.FilePath\x1a\r.zfs.StdReply\"\x00\x42\x06\xa2\x02\x03HLWb\x06proto3'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FILESTAT = _descriptor.Descriptor(
  name='FileStat',
  full_name='zfs.FileStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='st_ino', full_name='zfs.FileStat.st_ino', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_dev', full_name='zfs.FileStat.st_dev', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_mode', full_name='zfs.FileStat.st_mode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_nlink', full_name='zfs.FileStat.st_nlink', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_uid', full_name='zfs.FileStat.st_uid', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_gid', full_name='zfs.FileStat.st_gid', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_size', full_name='zfs.FileStat.st_size', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_atime', full_name='zfs.FileStat.st_atime', index=7,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_mtime', full_name='zfs.FileStat.st_mtime', index=8,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_ctime', full_name='zfs.FileStat.st_ctime', index=9,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=19,
  serialized_end=199,
)


_FILEPATH = _descriptor.Descriptor(
  name='FilePath',
  full_name='zfs.FilePath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='zfs.FilePath.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='zfs.FilePath.mode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=201,
  serialized_end=239,
)


_STDREPLY = _descriptor.Descriptor(
  name='StdReply',
  full_name='zfs.StdReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='zfs.StdReply.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='zfs.StdReply.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=241,
  serialized_end=290,
)


_TESTAUTHREQUEST = _descriptor.Descriptor(
  name='TestAuthRequest',
  full_name='zfs.TestAuthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='zfs.TestAuthRequest.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='st_mtime', full_name='zfs.TestAuthRequest.st_mtime', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=292,
  serialized_end=341,
)


_TESTAUTHREPLY = _descriptor.Descriptor(
  name='TestAuthReply',
  full_name='zfs.TestAuthReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='zfs.TestAuthReply.flag', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=343,
  serialized_end=372,
)


_FILEDATABLOCK = _descriptor.Descriptor(
  name='FileDataBlock',
  full_name='zfs.FileDataBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_block', full_name='zfs.FileDataBlock.data_block', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=374,
  serialized_end=409,
)


_DIRLISTBLOCK = _descriptor.Descriptor(
  name='DirListBlock',
  full_name='zfs.DirListBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dir_list_block', full_name='zfs.DirListBlock.dir_list_block', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=411,
  serialized_end=449,
)


_RENAMEMSG = _descriptor.Descriptor(
  name='RenameMsg',
  full_name='zfs.RenameMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='old', full_name='zfs.RenameMsg.old', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new', full_name='zfs.RenameMsg.new', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=451,
  serialized_end=488,
)

DESCRIPTOR.message_types_by_name['FileStat'] = _FILESTAT
DESCRIPTOR.message_types_by_name['FilePath'] = _FILEPATH
DESCRIPTOR.message_types_by_name['StdReply'] = _STDREPLY
DESCRIPTOR.message_types_by_name['TestAuthRequest'] = _TESTAUTHREQUEST
DESCRIPTOR.message_types_by_name['TestAuthReply'] = _TESTAUTHREPLY
DESCRIPTOR.message_types_by_name['FileDataBlock'] = _FILEDATABLOCK
DESCRIPTOR.message_types_by_name['DirListBlock'] = _DIRLISTBLOCK
DESCRIPTOR.message_types_by_name['RenameMsg'] = _RENAMEMSG

FileStat = _reflection.GeneratedProtocolMessageType('FileStat', (_message.Message,), dict(
  DESCRIPTOR = _FILESTAT,
  __module__ = 'zfs_pb2'
  # @@protoc_insertion_point(class_scope:zfs.FileStat)
  ))
_sym_db.RegisterMessage(FileStat)

FilePath = _reflection.GeneratedProtocolMessageType('FilePath', (_message.Message,), dict(
  DESCRIPTOR = _FILEPATH,
  __module__ = 'zfs_pb2'
  # @@protoc_insertion_point(class_scope:zfs.FilePath)
  ))
_sym_db.RegisterMessage(FilePath)

StdReply = _reflection.GeneratedProtocolMessageType('StdReply', (_message.Message,), dict(
  DESCRIPTOR = _STDREPLY,
  __module__ = 'zfs_pb2'
  # @@protoc_insertion_point(class_scope:zfs.StdReply)
  ))
_sym_db.RegisterMessage(StdReply)

TestAuthRequest = _reflection.GeneratedProtocolMessageType('TestAuthRequest', (_message.Message,), dict(
  DESCRIPTOR = _TESTAUTHREQUEST,
  __module__ = 'zfs_pb2'
  # @@protoc_insertion_point(class_scope:zfs.TestAuthRequest)
  ))
_sym_db.RegisterMessage(TestAuthRequest)

TestAuthReply = _reflection.GeneratedProtocolMessageType('TestAuthReply', (_message.Message,), dict(
  DESCRIPTOR = _TESTAUTHREPLY,
  __module__ = 'zfs_pb2'
  # @@protoc_insertion_point(class_scope:zfs.TestAuthReply)
  ))
_sym_db.RegisterMessage(TestAuthReply)

FileDataBlock = _reflection.GeneratedProtocolMessageType('FileDataBlock', (_message.Message,), dict(
  DESCRIPTOR = _FILEDATABLOCK,
  __module__ = 'zfs_pb2'
  # @@protoc_insertion_point(class_scope:zfs.FileDataBlock)
  ))
_sym_db.RegisterMessage(FileDataBlock)

DirListBlock = _reflection.GeneratedProtocolMessageType('DirListBlock', (_message.Message,), dict(
  DESCRIPTOR = _DIRLISTBLOCK,
  __module__ = 'zfs_pb2'
  # @@protoc_insertion_point(class_scope:zfs.DirListBlock)
  ))
_sym_db.RegisterMessage(DirListBlock)

RenameMsg = _reflection.GeneratedProtocolMessageType('RenameMsg', (_message.Message,), dict(
  DESCRIPTOR = _RENAMEMSG,
  __module__ = 'zfs_pb2'
  # @@protoc_insertion_point(class_scope:zfs.RenameMsg)
  ))
_sym_db.RegisterMessage(RenameMsg)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'\242\002\003HLW')
import abc
from grpc.beta import implementations as beta_implementations
from grpc.early_adopter import implementations as early_adopter_implementations
from grpc.framework.alpha import utilities as alpha_utilities
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
class EarlyAdopterZfsRpcServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetFileStat(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def TestAuth(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Fetch(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Store(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SetFileStat(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RemoveFile(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def MakeDir(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RemoveDir(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def FetchDir(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Rename(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def CreateFile(self, request, context):
    raise NotImplementedError()
class EarlyAdopterZfsRpcServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterZfsRpcStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetFileStat(self, request):
    raise NotImplementedError()
  GetFileStat.async = None
  @abc.abstractmethod
  def TestAuth(self, request):
    raise NotImplementedError()
  TestAuth.async = None
  @abc.abstractmethod
  def Fetch(self, request):
    raise NotImplementedError()
  Fetch.async = None
  @abc.abstractmethod
  def Store(self, request_iterator):
    raise NotImplementedError()
  Store.async = None
  @abc.abstractmethod
  def SetFileStat(self, request):
    raise NotImplementedError()
  SetFileStat.async = None
  @abc.abstractmethod
  def RemoveFile(self, request):
    raise NotImplementedError()
  RemoveFile.async = None
  @abc.abstractmethod
  def MakeDir(self, request):
    raise NotImplementedError()
  MakeDir.async = None
  @abc.abstractmethod
  def RemoveDir(self, request):
    raise NotImplementedError()
  RemoveDir.async = None
  @abc.abstractmethod
  def FetchDir(self, request):
    raise NotImplementedError()
  FetchDir.async = None
  @abc.abstractmethod
  def Rename(self, request):
    raise NotImplementedError()
  Rename.async = None
  @abc.abstractmethod
  def CreateFile(self, request):
    raise NotImplementedError()
  CreateFile.async = None
def early_adopter_create_ZfsRpc_server(servicer, port, private_key=None, certificate_chain=None):
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  method_service_descriptions = {
    "CreateFile": alpha_utilities.unary_unary_service_description(
      servicer.CreateFile,
      zfs_pb2.FilePath.FromString,
      zfs_pb2.StdReply.SerializeToString,
    ),
    "Fetch": alpha_utilities.unary_stream_service_description(
      servicer.Fetch,
      zfs_pb2.FilePath.FromString,
      zfs_pb2.FileDataBlock.SerializeToString,
    ),
    "FetchDir": alpha_utilities.unary_stream_service_description(
      servicer.FetchDir,
      zfs_pb2.FilePath.FromString,
      zfs_pb2.DirListBlock.SerializeToString,
    ),
    "GetFileStat": alpha_utilities.unary_unary_service_description(
      servicer.GetFileStat,
      zfs_pb2.FilePath.FromString,
      zfs_pb2.FileStat.SerializeToString,
    ),
    "MakeDir": alpha_utilities.unary_unary_service_description(
      servicer.MakeDir,
      zfs_pb2.FilePath.FromString,
      zfs_pb2.StdReply.SerializeToString,
    ),
    "RemoveDir": alpha_utilities.unary_unary_service_description(
      servicer.RemoveDir,
      zfs_pb2.FilePath.FromString,
      zfs_pb2.StdReply.SerializeToString,
    ),
    "RemoveFile": alpha_utilities.unary_unary_service_description(
      servicer.RemoveFile,
      zfs_pb2.FilePath.FromString,
      zfs_pb2.StdReply.SerializeToString,
    ),
    "Rename": alpha_utilities.unary_unary_service_description(
      servicer.Rename,
      zfs_pb2.RenameMsg.FromString,
      zfs_pb2.StdReply.SerializeToString,
    ),
    "SetFileStat": alpha_utilities.unary_unary_service_description(
      servicer.SetFileStat,
      zfs_pb2.FileStat.FromString,
      zfs_pb2.StdReply.SerializeToString,
    ),
    "Store": alpha_utilities.stream_unary_service_description(
      servicer.Store,
      zfs_pb2.FileDataBlock.FromString,
      zfs_pb2.StdReply.SerializeToString,
    ),
    "TestAuth": alpha_utilities.unary_unary_service_description(
      servicer.TestAuth,
      zfs_pb2.TestAuthRequest.FromString,
      zfs_pb2.TestAuthReply.SerializeToString,
    ),
  }
  return early_adopter_implementations.server("zfs.ZfsRpc", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_ZfsRpc_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  method_invocation_descriptions = {
    "CreateFile": alpha_utilities.unary_unary_invocation_description(
      zfs_pb2.FilePath.SerializeToString,
      zfs_pb2.StdReply.FromString,
    ),
    "Fetch": alpha_utilities.unary_stream_invocation_description(
      zfs_pb2.FilePath.SerializeToString,
      zfs_pb2.FileDataBlock.FromString,
    ),
    "FetchDir": alpha_utilities.unary_stream_invocation_description(
      zfs_pb2.FilePath.SerializeToString,
      zfs_pb2.DirListBlock.FromString,
    ),
    "GetFileStat": alpha_utilities.unary_unary_invocation_description(
      zfs_pb2.FilePath.SerializeToString,
      zfs_pb2.FileStat.FromString,
    ),
    "MakeDir": alpha_utilities.unary_unary_invocation_description(
      zfs_pb2.FilePath.SerializeToString,
      zfs_pb2.StdReply.FromString,
    ),
    "RemoveDir": alpha_utilities.unary_unary_invocation_description(
      zfs_pb2.FilePath.SerializeToString,
      zfs_pb2.StdReply.FromString,
    ),
    "RemoveFile": alpha_utilities.unary_unary_invocation_description(
      zfs_pb2.FilePath.SerializeToString,
      zfs_pb2.StdReply.FromString,
    ),
    "Rename": alpha_utilities.unary_unary_invocation_description(
      zfs_pb2.RenameMsg.SerializeToString,
      zfs_pb2.StdReply.FromString,
    ),
    "SetFileStat": alpha_utilities.unary_unary_invocation_description(
      zfs_pb2.FileStat.SerializeToString,
      zfs_pb2.StdReply.FromString,
    ),
    "Store": alpha_utilities.stream_unary_invocation_description(
      zfs_pb2.FileDataBlock.SerializeToString,
      zfs_pb2.StdReply.FromString,
    ),
    "TestAuth": alpha_utilities.unary_unary_invocation_description(
      zfs_pb2.TestAuthRequest.SerializeToString,
      zfs_pb2.TestAuthReply.FromString,
    ),
  }
  return early_adopter_implementations.stub("zfs.ZfsRpc", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)

class BetaZfsRpcServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetFileStat(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def TestAuth(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Fetch(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Store(self, request_iterator, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SetFileStat(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RemoveFile(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def MakeDir(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RemoveDir(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def FetchDir(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def Rename(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def CreateFile(self, request, context):
    raise NotImplementedError()

class BetaZfsRpcStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def GetFileStat(self, request, timeout):
    raise NotImplementedError()
  GetFileStat.future = None
  @abc.abstractmethod
  def TestAuth(self, request, timeout):
    raise NotImplementedError()
  TestAuth.future = None
  @abc.abstractmethod
  def Fetch(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def Store(self, request_iterator, timeout):
    raise NotImplementedError()
  Store.future = None
  @abc.abstractmethod
  def SetFileStat(self, request, timeout):
    raise NotImplementedError()
  SetFileStat.future = None
  @abc.abstractmethod
  def RemoveFile(self, request, timeout):
    raise NotImplementedError()
  RemoveFile.future = None
  @abc.abstractmethod
  def MakeDir(self, request, timeout):
    raise NotImplementedError()
  MakeDir.future = None
  @abc.abstractmethod
  def RemoveDir(self, request, timeout):
    raise NotImplementedError()
  RemoveDir.future = None
  @abc.abstractmethod
  def FetchDir(self, request, timeout):
    raise NotImplementedError()
  @abc.abstractmethod
  def Rename(self, request, timeout):
    raise NotImplementedError()
  Rename.future = None
  @abc.abstractmethod
  def CreateFile(self, request, timeout):
    raise NotImplementedError()
  CreateFile.future = None

def beta_create_ZfsRpc_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  request_deserializers = {
    ('zfs.ZfsRpc', 'CreateFile'): zfs_pb2.FilePath.FromString,
    ('zfs.ZfsRpc', 'Fetch'): zfs_pb2.FilePath.FromString,
    ('zfs.ZfsRpc', 'FetchDir'): zfs_pb2.FilePath.FromString,
    ('zfs.ZfsRpc', 'GetFileStat'): zfs_pb2.FilePath.FromString,
    ('zfs.ZfsRpc', 'MakeDir'): zfs_pb2.FilePath.FromString,
    ('zfs.ZfsRpc', 'RemoveDir'): zfs_pb2.FilePath.FromString,
    ('zfs.ZfsRpc', 'RemoveFile'): zfs_pb2.FilePath.FromString,
    ('zfs.ZfsRpc', 'Rename'): zfs_pb2.RenameMsg.FromString,
    ('zfs.ZfsRpc', 'SetFileStat'): zfs_pb2.FileStat.FromString,
    ('zfs.ZfsRpc', 'Store'): zfs_pb2.FileDataBlock.FromString,
    ('zfs.ZfsRpc', 'TestAuth'): zfs_pb2.TestAuthRequest.FromString,
  }
  response_serializers = {
    ('zfs.ZfsRpc', 'CreateFile'): zfs_pb2.StdReply.SerializeToString,
    ('zfs.ZfsRpc', 'Fetch'): zfs_pb2.FileDataBlock.SerializeToString,
    ('zfs.ZfsRpc', 'FetchDir'): zfs_pb2.DirListBlock.SerializeToString,
    ('zfs.ZfsRpc', 'GetFileStat'): zfs_pb2.FileStat.SerializeToString,
    ('zfs.ZfsRpc', 'MakeDir'): zfs_pb2.StdReply.SerializeToString,
    ('zfs.ZfsRpc', 'RemoveDir'): zfs_pb2.StdReply.SerializeToString,
    ('zfs.ZfsRpc', 'RemoveFile'): zfs_pb2.StdReply.SerializeToString,
    ('zfs.ZfsRpc', 'Rename'): zfs_pb2.StdReply.SerializeToString,
    ('zfs.ZfsRpc', 'SetFileStat'): zfs_pb2.StdReply.SerializeToString,
    ('zfs.ZfsRpc', 'Store'): zfs_pb2.StdReply.SerializeToString,
    ('zfs.ZfsRpc', 'TestAuth'): zfs_pb2.TestAuthReply.SerializeToString,
  }
  method_implementations = {
    ('zfs.ZfsRpc', 'CreateFile'): face_utilities.unary_unary_inline(servicer.CreateFile),
    ('zfs.ZfsRpc', 'Fetch'): face_utilities.unary_stream_inline(servicer.Fetch),
    ('zfs.ZfsRpc', 'FetchDir'): face_utilities.unary_stream_inline(servicer.FetchDir),
    ('zfs.ZfsRpc', 'GetFileStat'): face_utilities.unary_unary_inline(servicer.GetFileStat),
    ('zfs.ZfsRpc', 'MakeDir'): face_utilities.unary_unary_inline(servicer.MakeDir),
    ('zfs.ZfsRpc', 'RemoveDir'): face_utilities.unary_unary_inline(servicer.RemoveDir),
    ('zfs.ZfsRpc', 'RemoveFile'): face_utilities.unary_unary_inline(servicer.RemoveFile),
    ('zfs.ZfsRpc', 'Rename'): face_utilities.unary_unary_inline(servicer.Rename),
    ('zfs.ZfsRpc', 'SetFileStat'): face_utilities.unary_unary_inline(servicer.SetFileStat),
    ('zfs.ZfsRpc', 'Store'): face_utilities.stream_unary_inline(servicer.Store),
    ('zfs.ZfsRpc', 'TestAuth'): face_utilities.unary_unary_inline(servicer.TestAuth),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_ZfsRpc_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  import zfs_pb2
  request_serializers = {
    ('zfs.ZfsRpc', 'CreateFile'): zfs_pb2.FilePath.SerializeToString,
    ('zfs.ZfsRpc', 'Fetch'): zfs_pb2.FilePath.SerializeToString,
    ('zfs.ZfsRpc', 'FetchDir'): zfs_pb2.FilePath.SerializeToString,
    ('zfs.ZfsRpc', 'GetFileStat'): zfs_pb2.FilePath.SerializeToString,
    ('zfs.ZfsRpc', 'MakeDir'): zfs_pb2.FilePath.SerializeToString,
    ('zfs.ZfsRpc', 'RemoveDir'): zfs_pb2.FilePath.SerializeToString,
    ('zfs.ZfsRpc', 'RemoveFile'): zfs_pb2.FilePath.SerializeToString,
    ('zfs.ZfsRpc', 'Rename'): zfs_pb2.RenameMsg.SerializeToString,
    ('zfs.ZfsRpc', 'SetFileStat'): zfs_pb2.FileStat.SerializeToString,
    ('zfs.ZfsRpc', 'Store'): zfs_pb2.FileDataBlock.SerializeToString,
    ('zfs.ZfsRpc', 'TestAuth'): zfs_pb2.TestAuthRequest.SerializeToString,
  }
  response_deserializers = {
    ('zfs.ZfsRpc', 'CreateFile'): zfs_pb2.StdReply.FromString,
    ('zfs.ZfsRpc', 'Fetch'): zfs_pb2.FileDataBlock.FromString,
    ('zfs.ZfsRpc', 'FetchDir'): zfs_pb2.DirListBlock.FromString,
    ('zfs.ZfsRpc', 'GetFileStat'): zfs_pb2.FileStat.FromString,
    ('zfs.ZfsRpc', 'MakeDir'): zfs_pb2.StdReply.FromString,
    ('zfs.ZfsRpc', 'RemoveDir'): zfs_pb2.StdReply.FromString,
    ('zfs.ZfsRpc', 'RemoveFile'): zfs_pb2.StdReply.FromString,
    ('zfs.ZfsRpc', 'Rename'): zfs_pb2.StdReply.FromString,
    ('zfs.ZfsRpc', 'SetFileStat'): zfs_pb2.StdReply.FromString,
    ('zfs.ZfsRpc', 'Store'): zfs_pb2.StdReply.FromString,
    ('zfs.ZfsRpc', 'TestAuth'): zfs_pb2.TestAuthReply.FromString,
  }
  cardinalities = {
    'CreateFile': cardinality.Cardinality.UNARY_UNARY,
    'Fetch': cardinality.Cardinality.UNARY_STREAM,
    'FetchDir': cardinality.Cardinality.UNARY_STREAM,
    'GetFileStat': cardinality.Cardinality.UNARY_UNARY,
    'MakeDir': cardinality.Cardinality.UNARY_UNARY,
    'RemoveDir': cardinality.Cardinality.UNARY_UNARY,
    'RemoveFile': cardinality.Cardinality.UNARY_UNARY,
    'Rename': cardinality.Cardinality.UNARY_UNARY,
    'SetFileStat': cardinality.Cardinality.UNARY_UNARY,
    'Store': cardinality.Cardinality.STREAM_UNARY,
    'TestAuth': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'zfs.ZfsRpc', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)