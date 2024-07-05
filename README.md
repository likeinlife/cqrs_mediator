# Description

Mediator pattern impl

# Docs

[WIKI](https://github.com/likeinlife/cqrs_mediator/wiki)

# Available

- Dispatchers:
    - Command
    - Query
- Observers:
    - Event
- Entities:
    - Command
    - Event
    - Query
- Middlewares:
  - Middleware

# Usecases

## Command/Event/Query

```python
from dataclasses import dataclass

from mediator.dispatchers import CommandDispatcherImpl
from mediator.entities import Command
from mediator.interfaces.handlers import ICommandHandler

@dataclass
class IntCommand(Command[int]):
    answer: int


class IntCommandHandler(ICommandHandler[IntCommand, int]):
    async def __call__(self, request: IntCommand) -> int:
        return request.answer

async def main():
    c = CommandDispatcherImpl()

    c.register(IntCommand, IntCommandHandler())

    await c.handle(IntCommand(1))
```

## Middleware

```python
from dataclasses import dataclass

from mediator.dispatchers import CommandDispatcherImpl
from mediator.entities import Command, Request
from mediator.interfaces.handlers import ICommandHandler
from mediator.middlewares.base import Middleware


class SimpleMiddleware(Middleware):
    async def __call__(self, request: Request):
        return await self.call_next(request)

@dataclass
class IntCommand(Command[int]):
    answer: int


class IntCommandHandler(ICommandHandler[IntCommand, int]):
    async def __call__(self, request: IntCommand) -> int:
        return request.answer

async def main():
    c = CommandDispatcherImpl(middlewares=[SimpleMiddleware])

    c.register(IntCommand, IntCommandHandler())

    await c.handle(IntCommand(1))
```
# Tests

- `pytest tests`

# Additional

Inspired by [didator](https://github.com/SamWarden/didiator)