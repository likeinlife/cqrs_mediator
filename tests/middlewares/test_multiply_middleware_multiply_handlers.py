from meator.dispatchers import CommandDispatcherImpl
from tests.mock.commands import IntCommand, IntCommandHandler, StringCommand, StringCommandHandler
from tests.mock.middleware import StateChangerMiddleware
from tests.mock.state import State


async def test_dispatcher_middleware_sequence():
    states = [State() for _ in range(10)]
    middlewares = [StateChangerMiddleware(state) for state in states]
    c = CommandDispatcherImpl(middlewares=middlewares)

    int_handler = IntCommandHandler()
    string_handler = StringCommandHandler()
    c.register(IntCommand, int_handler)
    c.register(StringCommand, string_handler)

    assert await c.handle(IntCommand(1)) == 1
    assert all(i.modified for i in states)
