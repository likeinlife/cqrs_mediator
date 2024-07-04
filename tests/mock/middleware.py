from dataclasses import dataclass

from mediator.entities.request import Request
from mediator.middlewares.base import Middleware
from tests.mock.state import State


@dataclass(eq=False)
class StateChangerMiddleware(Middleware):
    state: State

    async def __call__(self, request: Request):
        self.state.modified = True
        return await super().__call__(request)
