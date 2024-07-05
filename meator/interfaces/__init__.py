"""Interfaces package."""

from .dispatcher import IDispatcher
from .handlers import ICommandHandler, IEventHandler, IHandler, IQueryHandler
from .middleware import IMiddleware
from .observer import IObserver

__all__ = (
    "IDispatcher",
    "IObserver",
    "IMiddleware",
    "ICommandHandler",
    "IEventHandler",
    "IHandler",
    "IQueryHandler",
)
