import random

from mediator.observers import EventObserverImpl
from tests.mock.events import IntEvent, IntEventHandler
from tests.mock.state import State


async def test_observer_middleware_sequence():
    states = [State() for _ in range(10)]
    handlers = [IntEventHandler(state) for state in states]
    c = EventObserverImpl()

    c.register(IntEvent, handlers)

    answer = random.randint(0, 100)

    await c.handle(IntEvent(answer))
    assert all(i.modified for i in states)
