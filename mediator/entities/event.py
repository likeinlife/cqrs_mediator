from typing import TypeVar

from .request import Request

ERes = TypeVar("ERes")


class Event(Request[None]):
    """Base event entity."""
