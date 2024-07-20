"""Interfaces package."""

from .dispatcher import ICommandDispatcher, IDispatcher, IQueryDispatcher
from .handlers import ICommandHandler, IEventHandler, IHandler, IQueryHandler
from .middleware import IMiddleware
from .observer import IEventObserver, IObserver

__all__ = (
    "IDispatcher",
    "IObserver",
    "IMiddleware",
    "ICommandHandler",
    "IEventHandler",
    "IHandler",
    "IQueryHandler",
    "ICommandDispatcher",
    "IQueryDispatcher",
    "IEventObserver",
)
