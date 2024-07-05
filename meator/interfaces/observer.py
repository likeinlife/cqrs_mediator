import abc
import typing as tp

from meator.entities import Request
from meator.interfaces.handlers.request import IHandler

Res = tp.TypeVar("Res")
Req = tp.TypeVar("Req", bound=Request)


class IObserver(abc.ABC):
    @abc.abstractmethod
    def register(self, request: type[Req], handlers: tp.Sequence[IHandler[Req, Res]]) -> None:
        """Register handler for request."""

    @abc.abstractmethod
    async def handle(self, request: Request[None]) -> None:
        """Handle request."""
