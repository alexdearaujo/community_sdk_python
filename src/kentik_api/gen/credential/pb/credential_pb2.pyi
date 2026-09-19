import datetime
from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from kentik.user.v202211 import user_pb2 as _user_pb2
from kentik.vault.v202312alpha1 import vault_pb2 as _vault_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CredentialGroup(_message.Message):
    __slots__ = (
        "id",
        "name",
        "version",
        "description",
        "type",
        "cdate",
        "edate",
        "created_by",
        "credentials",
        "labels",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CDATE_FIELD_NUMBER: _ClassVar[int]
    EDATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    version: int
    description: str
    type: _vault_pb2.SecretType
    cdate: _timestamp_pb2.Timestamp
    edate: _timestamp_pb2.Timestamp
    created_by: _user_pb2.User
    credentials: _containers.RepeatedCompositeFieldContainer[_vault_pb2.Secret]
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        version: _Optional[int] = ...,
        description: _Optional[str] = ...,
        type: _Optional[_Union[_vault_pb2.SecretType, str]] = ...,
        cdate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        edate: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        created_by: _Optional[_Union[_user_pb2.User, _Mapping]] = ...,
        credentials: _Optional[_Iterable[_Union[_vault_pb2.Secret, _Mapping]]] = ...,
        labels: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class GetCredentialGroupRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCredentialGroupResponse(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: CredentialGroup
    def __init__(
        self, group: _Optional[_Union[CredentialGroup, _Mapping]] = ...
    ) -> None: ...

class ListCredentialGroupRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCredentialGroupResponse(_message.Message):
    __slots__ = ("groups", "invalid_count")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    INVALID_COUNT_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[CredentialGroup]
    invalid_count: int
    def __init__(
        self,
        groups: _Optional[_Iterable[_Union[CredentialGroup, _Mapping]]] = ...,
        invalid_count: _Optional[int] = ...,
    ) -> None: ...
