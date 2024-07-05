from typing import TypeVar

from .request import Request

CRes = TypeVar("CRes")


class Command(Request[CRes]):
    """Base command entity."""
