import random
from string import ascii_lowercase

from meator.dispatchers import CommandDispatcherImpl
from tests.mock.commands import IntCommand, IntCommandHandler, StringCommand, StringCommandHandler


async def test_dispatcher_multiply_handlers_pipeline():
    c = CommandDispatcherImpl()

    c.register(IntCommand, IntCommandHandler())
    c.register(StringCommand, StringCommandHandler())

    answer = random.randint(0, 100)
    string = random.choice(ascii_lowercase)

    assert await c.handle(IntCommand(answer)) == answer
    assert await c.handle(StringCommand(string)) == string
