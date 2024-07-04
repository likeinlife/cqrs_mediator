import abc
import typing as tp

from mediator.entities import Request
from mediator.interfaces.handlers.request import IHandler

Res = tp.TypeVar("Res")
Req = tp.TypeVar("Req", bound=Request)


class IDispatcher(abc.ABC):
    @abc.abstractmethod
    def register(self, request: type[Req], handler: IHandler[Req, Res]) -> None:
        """Register handler for request."""

    @abc.abstractmethod
    async def handle(self, request: Request[Res]) -> Res:
        """Handle request."""
