import abc
import typing as tp

from meator.entities import Request

HRes = tp.TypeVar("HRes")
RType = tp.TypeVar("RType", bound=Request)


class Handler(abc.ABC, tp.Generic[RType, HRes]):
    @abc.abstractmethod
    async def __call__(self, request: RType) -> HRes: ...
