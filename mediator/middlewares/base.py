import typing as tp

from mediator.entities.request import Request
from mediator.interfaces.middleware import IMiddleware
from mediator.interfaces.types import CallNextType

Res = tp.TypeVar("Res")


class Middleware(IMiddleware):
    @tp.final
    def set_next(self, call_next: CallNextType) -> tp.Self:
        self.call_next = call_next
        return self

    async def __call__(self, request: Request) -> tp.Any:
        return await self.call_next(request)
