import typing as tp
from typing import TypeVar

from meator._constants import _sentinel
from meator._utils.sentinel_default import get_default_sentinel
from meator.dispatchers.errors import HandlerNotFoundError
from meator.entities.request import Request
from meator.interfaces.dispatcher import IDispatcher
from meator.interfaces.handlers.request import IHandler
from meator.middlewares import wrap_handler
from meator.middlewares.base import Middleware

Res = TypeVar("Res")
RType = TypeVar("RType", bound=Request)


class BaseDispatcherImpl(IDispatcher):
    def __init__(
        self,
        *,
        middlewares: tp.Sequence[Middleware] = _sentinel,
        handlers: dict[type[Request], IHandler] = _sentinel,
    ) -> None:
        self._middlewares = get_default_sentinel(middlewares, [])
        self._handlers = get_default_sentinel(handlers, {})

    def register(self, request: type[RType], handler: IHandler[RType, Res]) -> None:
        self._handlers[request] = wrap_handler(self._middlewares, handler)

    async def handle(self, request: Request[Res]) -> Res:
        handler = self._get_handler(request)
        return await handler(request)

    def _get_handler(self, request: Request[Res]) -> IHandler[Request[Res], Res]:
        if (r_type := type(request)) not in self._handlers:
            raise HandlerNotFoundError(r_type)

        return self._handlers[r_type]
