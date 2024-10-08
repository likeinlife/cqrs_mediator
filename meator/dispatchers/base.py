import typing as tp
from typing import TypeVar

from meator._constants import _UNSET
from meator._utils.sentinel_default import get_default_sentinel
from meator.dispatchers.errors import HandlerNotFoundError
from meator.entities.request import Request
from meator.interfaces.dispatcher import Dispatcher
from meator.interfaces.handlers.request import Handler
from meator.interfaces.middleware import Middleware
from meator.interfaces.types import CallNextType
from meator.middlewares import wrap_handler_with_middleware

Res = TypeVar("Res")
RType = TypeVar("RType", bound=Request)


class DispatcherImpl(Dispatcher):
    def __init__(
        self,
        *,
        middlewares: tp.Sequence[Middleware] = _UNSET,
        handlers: dict[type[Request], CallNextType[Request, tp.Any]] = _UNSET,
    ) -> None:
        self._middlewares = get_default_sentinel(middlewares, [])
        self._handlers = get_default_sentinel(handlers, {})

    def register(self, request: type[RType], handler: Handler[RType, Res]) -> None:
        self._handlers[request] = wrap_handler_with_middleware(self._middlewares, handler)

    async def handle(self, request: Request[Res]) -> Res:
        handler = self._get_handler(type(request))
        return await handler(request)

    def _get_handler(self, request_type: type[Request[Res]]) -> CallNextType[RType, Res]:
        if request_type not in self._handlers:
            raise HandlerNotFoundError(request_type)

        return self._handlers[request_type]
