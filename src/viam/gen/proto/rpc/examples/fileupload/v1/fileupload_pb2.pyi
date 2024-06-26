"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class UploadFileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    CHUNK_DATA_FIELD_NUMBER: builtins.int
    name: builtins.str
    chunk_data: builtins.bytes

    def __init__(self, *, name: builtins.str=..., chunk_data: builtins.bytes=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['chunk_data', b'chunk_data', 'data', b'data', 'name', b'name']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['chunk_data', b'chunk_data', 'data', b'data', 'name', b'name']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['data', b'data']) -> typing.Literal['name', 'chunk_data'] | None:
        ...
global___UploadFileRequest = UploadFileRequest

@typing.final
class UploadFileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    name: builtins.str
    size: builtins.int

    def __init__(self, *, name: builtins.str=..., size: builtins.int=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['name', b'name', 'size', b'size']) -> None:
        ...
global___UploadFileResponse = UploadFileResponse