"""Dispatchers package.

Available:
    - Command
    - Query
    - Base

Base is useful for creating own dispatcher.
"""

from .base import BaseDispatcherImpl
from .command import CommandDispatcherImpl
from .query import QueryDispatcherImpl

__all__ = (
    "BaseDispatcherImpl",
    "CommandDispatcherImpl",
    "QueryDispatcherImpl",
)
