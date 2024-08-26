import abc
import typing as tp

from meator.entities import Request
from meator.interfaces.handlers.request import Handler


class IMiddleware(abc.ABC):
    @abc.abstractmethod
    async def __call__(self, call_next: Handler, request: Request) -> tp.Any: ...
