import random

from mediator.dispatchers import CommandDispatcherImpl
from tests.mock.commands import IntCommand, IntCommandHandler
from tests.mock.middleware import StateChangerMiddleware
from tests.mock.state import State


async def test_dispatcher_middleware():
    state = State()
    c = CommandDispatcherImpl(middlewares=[StateChangerMiddleware(state)])

    c.register(IntCommand, IntCommandHandler())

    answer = random.randint(0, 100)

    assert await c.handle(IntCommand(answer)) == answer
    assert state.modified
