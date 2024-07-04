import random

from mediator.observers import EventObserverImpl
from tests.mock.events import IntEvent, IntEventHandler
from tests.mock.middleware import StateChangerMiddleware
from tests.mock.state import State


async def test_observer_middleware():
    middleware_state = State()
    handler_state = State()
    middleware = StateChangerMiddleware(middleware_state)
    c = EventObserverImpl(middlewares=[middleware])

    c.register(IntEvent, [IntEventHandler(handler_state)])

    answer = random.randint(0, 100)

    await c.handle(IntEvent(answer))
    assert middleware_state.modified
    assert handler_state.modified
