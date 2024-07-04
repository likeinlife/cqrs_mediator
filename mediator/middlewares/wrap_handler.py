import typing as tp
from functools import reduce

from mediator.interfaces.handlers.request import IHandler
from mediator.interfaces.types import CallNextType
from mediator.middlewares.base import Middleware


def wrap_handler(middlewares: tp.Sequence[Middleware], handler: IHandler) -> CallNextType:
    return reduce(lambda x, y: y.set_next(x), middlewares, handler)
