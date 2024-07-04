import typing as tp

from mediator.entities import Request
from mediator.interfaces.handlers import IHandler
from mediator.interfaces.types import CallNextType


class IMiddleware(IHandler[Request, tp.Any]):
    call_next: CallNextType
