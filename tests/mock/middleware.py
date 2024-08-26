import typing as tp
from dataclasses import dataclass

from meator.entities.request import Request
from meator.interfaces.handlers.request import Handler
from meator.interfaces.middleware import Middleware
from tests.mock.state import State


@dataclass(eq=False)
class StateChangerMiddleware(Middleware):
    state: State

    async def __call__(self, call_next: Handler, request: Request) -> tp.Any:
        self.state.modified = True
        return await call_next(request)
