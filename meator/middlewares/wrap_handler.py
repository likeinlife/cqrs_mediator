import functools
import typing as tp

from meator.entities import Request
from meator.interfaces.handlers.request import IHandler
from meator.interfaces.middleware import IMiddleware

Res = tp.TypeVar("Res")


def wrap_handler_with_middleware(
    middlewares: tp.Sequence[IMiddleware],
    handler: IHandler,
) -> tp.Callable[[Request[Res]], tp.Awaitable[Res]]:
    call_next: tp.Callable[[Request[Res]], tp.Awaitable[Res]] = handler
    for middleware in middlewares:
        call_next = functools.partial(middleware, call_next)

    return call_next
