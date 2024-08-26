from dataclasses import dataclass

from meator.entities import Command
from meator.interfaces.handlers import CommandHandler


@dataclass
class IntCommand(Command[int]):
    answer: int


@dataclass
class StringCommand(Command[int]):
    string: str


class IntCommandHandler(CommandHandler[IntCommand, int]):
    async def __call__(self, request: IntCommand) -> int:
        return request.answer


class StringCommandHandler(CommandHandler[StringCommand, str]):
    async def __call__(self, request: StringCommand) -> str:
        return request.string
