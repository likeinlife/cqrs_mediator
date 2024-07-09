import typing as tp

from meator.entities import Request

Res = tp.TypeVar("Res")
ReqType = tp.TypeVar("ReqType", bound=Request)

CallNextType: tp.TypeAlias = tp.Callable[[ReqType], tp.Awaitable[Res]]
