from dataclasses import dataclass

from meator.entities import Event
from meator.interfaces.handlers import EventHandler
from tests.mock.state import State


@dataclass
class IntEvent(Event):
    answer: int


@dataclass
class IntEventHandler(EventHandler[IntEvent]):
    state: State

    async def __call__(self, request: IntEvent) -> None:  # noqa: ARG002
        self.state.modified = True
