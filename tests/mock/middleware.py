from dataclasses import dataclass

from meator.entities.request import Request
from meator.interfaces.handlers.request import IHandler
from meator.interfaces.middleware import IMiddleware
from tests.mock.state import State


@dataclass(eq=False)
class StateChangerMiddleware(IMiddleware):
    state: State

    async def __call__(self, handler: IHandler, request: Request):
        self.state.modified = True
        return await handler(request)
