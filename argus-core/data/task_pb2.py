# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntask.proto\x12\nargus_core\"\xbc\x01\n\x04Task\x12\x13\n\x06stdout\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06stderr\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\texit_code\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\'\n\x06status\x18\x04 \x01(\x0e\x32\x12.argus_core.StatusH\x03\x88\x01\x01\x12\x11\n\x04name\x18\x05 \x01(\tH\x04\x88\x01\x01\x42\t\n\x07_stdoutB\t\n\x07_stderrB\x0c\n\n_exit_codeB\t\n\x07_statusB\x07\n\x05_name*H\n\x06Status\x12\n\n\x06QUEUED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x0c\n\x08\x46INISHED\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STATUS']._serialized_start=217
  _globals['_STATUS']._serialized_end=289
  _globals['_TASK']._serialized_start=27
  _globals['_TASK']._serialized_end=215
# @@protoc_insertion_point(module_scope)