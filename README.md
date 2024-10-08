# Meator

[![image](https://img.shields.io/pypi/v/meator.svg)](https://pypi.python.org/pypi/meator)
<a href="http://mypy-lang.org/" target="_blank"><img src="https://img.shields.io/badge/mypy-checked-1F5082.svg" alt="Mypy checked"></a>
[![codecov](https://codecov.io/gh/likeinlife/cqrs_mediator/graph/badge.svg?token=BVDRFQ61R6)](https://codecov.io/gh/likeinlife/cqrs_mediator)
[![image](https://img.shields.io/pypi/l/meator.svg)](https://github.com/likeinlife/cqrs_mediator/blob/main/LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![image](https://img.shields.io/pypi/pyversions/meator.svg)](https://pypi.python.org/pypi/meator)

Python CQRS pattern implementation.

[**Docs**](https://github.com/likeinlife/cqrs_mediator/wiki)

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
- Middlewares

# Usecases

## Command/Event/Query

```python
from dataclasses import dataclass

from meator.dispatchers import CommandDispatcherImpl
from meator.entities import Command
from meator.interfaces import CommandHandler


@dataclass
class IntCommand(Command[int]):
    answer: int


class IntCommandHandler(CommandHandler[IntCommand, int]):
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
from meator.interfaces import CommandHandler, Handler, Middleware


class SimpleMiddleware(Middleware):
    async def __call__(self, call_next: Handler, request: Request):
        return await call_next(request)


@dataclass
class IntCommand(Command[int]):
    answer: int


class IntCommandHandler(CommandHandler[IntCommand, int]):
    async def __call__(self, request: IntCommand) -> int:
        return request.answer


async def main():
    c = CommandDispatcherImpl(middlewares=[SimpleMiddleware()])

    c.register(IntCommand, IntCommandHandler())

    await c.handle(IntCommand(1))
```
# Tests

- `pytest tests`

# Additional

Inspired by [didator](https://github.com/SamWarden/didiator)
