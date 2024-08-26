from meator.dispatchers.base import DispatcherImpl
from meator.interfaces import CommandDispatcher


class CommandDispatcherImpl(DispatcherImpl, CommandDispatcher):
    """Command dispatcher."""
