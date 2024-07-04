import random

from mediator.observers import EventObserverImpl
from tests.mock.events import IntEvent, IntEventHandler
from tests.mock.state import State


async def test_observer_pipeline():
    state = State()
    c = EventObserverImpl()

    c.register(IntEvent, [IntEventHandler(state)])

    answer = random.randint(0, 100)

    await c.handle(IntEvent(answer))
    assert state.modified
