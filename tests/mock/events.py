from dataclasses import dataclass

from mediator.entities import Event
from mediator.interfaces.handlers import IEventHandler
from tests.mock.state import State


@dataclass
class IntEvent(Event):
    answer: int


@dataclass
class IntEventHandler(IEventHandler[IntEvent, None]):
    state: State

    async def __call__(self, request: IntEvent) -> None:  # noqa: ARG002
        self.state.modified = True
