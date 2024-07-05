import typing as tp

from meator.entities.request import Request
from meator.interfaces.middleware import IMiddleware
from meator.interfaces.types import CallNextType

Res = tp.TypeVar("Res")


class Middleware(IMiddleware):
    @tp.final
    def set_next(self, call_next: CallNextType) -> tp.Self:
        self.call_next = call_next
        return self

    async def __call__(self, request: Request) -> tp.Any:
        return await self.call_next(request)
