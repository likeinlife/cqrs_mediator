import pytest

from mediator.dispatchers import CommandDispatcherImpl
from mediator.dispatchers.errors import HandlerNotFoundError
from tests.mock.commands import IntCommand


async def test_dispatcher_no_handler():
    c = CommandDispatcherImpl()

    with pytest.raises(HandlerNotFoundError):
        await c.handle(IntCommand(1))
