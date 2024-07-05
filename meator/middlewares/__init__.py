"""Middlewares package.

Example middleware:

```python
from meator.middlewares import Middleware

class CustomMiddleware(Middleware):
    async def __call__(self, request: Request) -> tp.Any:
        ...
        result = await self.call_next(request)
        ...
        return result
```
"""

from .base import Middleware
from .wrap_handler import wrap_handler

__all__ = ("Middleware", "wrap_handler")
