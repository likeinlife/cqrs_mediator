import typing as tp
from typing import TypeVar

from meator._constants import _sentinel
from meator._utils.sentinel_default import get_default_sentinel
from meator.entities.request import Request
from meator.interfaces.handlers.request import IHandler
from meator.interfaces.observer import IObserver
from meator.middlewares import wrap_handler
from meator.middlewares.base import Middleware

Res = TypeVar("Res")
Req = TypeVar("Req", bound=Request)


class BaseObserverImpl(IObserver):
    def __init__(
        self,
        *,
        middlewares: tp.Sequence[Middleware] = _sentinel,
        handlers: dict[type[Request], tp.Sequence[IHandler]] = _sentinel,
    ) -> None:
        self._middlewares = get_default_sentinel(middlewares, ())
        self._handlers = get_default_sentinel(handlers, {})

    def register(self, request: type[Req], handlers: tp.Sequence[IHandler[Req, Res]]) -> None:
        self._handlers[request] = tuple(wrap_handler(self._middlewares, handler) for handler in handlers)

    async def handle(self, request: Request[None]) -> None:
        handlers = self._get_handler(request)
        for handler in handlers:
            await handler(request)

    def _get_handler(self, request: Request[Res]) -> tp.Sequence[IHandler[Request, Res]]:
        return self._handlers.get(type(request), ())
