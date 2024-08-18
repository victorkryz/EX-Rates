from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("currency_code",)
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    currency_code: str
    def __init__(self, currency_code: _Optional[str] = ...) -> None: ...

class Rates(_message.Message):
    __slots__ = ("entries",)
    class Rate(_message.Message):
        __slots__ = ("currency", "value")
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        currency: str
        value: float
        def __init__(self, currency: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[Rates.Rate]
    def __init__(self, entries: _Optional[_Iterable[_Union[Rates.Rate, _Mapping]]] = ...) -> None: ...
