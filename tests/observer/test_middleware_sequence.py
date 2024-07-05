import random

from meator.observers import EventObserverImpl
from tests.mock.events import IntEvent, IntEventHandler
from tests.mock.middleware import StateChangerMiddleware
from tests.mock.state import State


async def test_observer_middleware_sequence():
    states = [State() for _ in range(10)]
    middlewares = [StateChangerMiddleware(state) for state in states]
    handler_state = State()
    c = EventObserverImpl(middlewares=middlewares)

    c.register(IntEvent, [IntEventHandler(handler_state)])

    answer = random.randint(0, 100)

    await c.handle(IntEvent(answer))
    assert all(i.modified for i in states)
    assert handler_state.modified
