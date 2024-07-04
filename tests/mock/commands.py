from dataclasses import dataclass

from mediator.entities import Command
from mediator.interfaces.handlers import ICommandHandler


@dataclass
class IntCommand(Command[int]):
    answer: int


class IntCommandHandler(ICommandHandler[IntCommand, int]):
    async def __call__(self, request: IntCommand) -> int:
        return request.answer
