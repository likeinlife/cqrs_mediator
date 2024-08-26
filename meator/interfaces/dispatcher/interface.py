import abc
import typing as tp

from meator.entities import Request
from meator.interfaces.handlers.request import Handler

Res = tp.TypeVar("Res")
Req = tp.TypeVar("Req", bound=Request)


class Dispatcher(abc.ABC):
    @abc.abstractmethod
    def register(self, request: type[Req], handler: Handler[Req, Res]) -> None:
        """Register handler for request."""

    @abc.abstractmethod
    async def handle(self, request: Request[Res]) -> Res:
        """Handle request."""
