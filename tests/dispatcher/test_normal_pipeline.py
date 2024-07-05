import random

from meator.dispatchers import CommandDispatcherImpl
from tests.mock.commands import IntCommand, IntCommandHandler


async def test_dispatcher_pipeline():
    c = CommandDispatcherImpl()

    c.register(IntCommand, IntCommandHandler())

    answer = random.randint(0, 100)

    assert await c.handle(IntCommand(answer)) == answer
