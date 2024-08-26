import typing as tp
from typing import TypeVar

from meator._constants import _UNSET
from meator._utils.sentinel_default import get_default_sentinel
from meator.entities.request import Request
from meator.interfaces.handlers.request import Handler
from meator.interfaces.middleware import IMiddleware
from meator.interfaces.observer import Observer
from meator.interfaces.types import CallNextType
from meator.middlewares import wrap_handler_with_middleware

Res = TypeVar("Res")
RType = TypeVar("RType", bound=Request)


class ObserverImpl(Observer):
    def __init__(
        self,
        *,
        middlewares: tp.Sequence[IMiddleware] = _UNSET,
        handlers: dict[type[Request], tp.Sequence[CallNextType[Request, tp.Any]]] = _UNSET,
    ) -> None:
        self._middlewares = get_default_sentinel(middlewares, ())
        self._handlers = get_default_sentinel(handlers, {})

    def register(self, request: type[RType], handlers: tp.Sequence[Handler[RType, Res]]) -> None:
        self._handlers[request] = [wrap_handler_with_middleware(self._middlewares, handler) for handler in handlers]

    async def handle(self, request: Request[None]) -> None:
        handlers = self._get_handler(request)
        for handler in handlers:
            await handler(request)

    def _get_handler(self, request: Request[Res]) -> tp.Sequence[CallNextType[Request, Res]]:
        return self._handlers.get(type(request), ())
