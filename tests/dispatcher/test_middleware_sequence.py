import random

from mediator.dispatchers import CommandDispatcherImpl
from tests.mock.commands import IntCommand, IntCommandHandler
from tests.mock.middleware import StateChangerMiddleware
from tests.mock.state import State


async def test_dispatcher_middleware_sequence():
    states = [State() for _ in range(10)]
    middlewares = [StateChangerMiddleware(state) for state in states]
    c = CommandDispatcherImpl(middlewares=middlewares)

    c.register(IntCommand, IntCommandHandler())

    answer = random.randint(0, 100)

    assert await c.handle(IntCommand(answer)) == answer
    assert all(state.modified for state in states)
