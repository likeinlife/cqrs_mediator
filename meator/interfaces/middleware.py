import typing as tp

from meator.entities import Request
from meator.interfaces.handlers import IHandler
from meator.interfaces.types import CallNextType


class IMiddleware(IHandler[Request, tp.Any]):
    call_next: CallNextType
