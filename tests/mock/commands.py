from dataclasses import dataclass

from meator.entities import Command
from meator.interfaces.handlers import ICommandHandler


@dataclass
class IntCommand(Command[int]):
    answer: int


class IntCommandHandler(ICommandHandler[IntCommand, int]):
    async def __call__(self, request: IntCommand) -> int:
        return request.answer
