# Description

Mediator pattern impl

[PYPI](https://pypi.org/project/meator/)

[WIKI](https://github.com/likeinlife/cqrs_mediator/wiki)

# Installation

```shell
pip install meator
```

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

from meator.dispatchers import CommandDispatcherImpl
from meator.entities import Command
from meator.interfaces.handlers import ICommandHandler

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

from meator.dispatchers import CommandDispatcherImpl
from meator.entities import Command, Request
from meator.interfaces.handlers import ICommandHandler
from meator.middlewares.base import Middleware


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