from typing import TypeVar

from .request import Request

QRes = TypeVar("QRes")


class Query(Request[QRes]):
    """Base entity."""
