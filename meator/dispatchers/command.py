from meator.dispatchers.base import BaseDispatcherImpl
from meator.interfaces import ICommandDispatcher


class CommandDispatcherImpl(BaseDispatcherImpl, ICommandDispatcher):
    """Command dispatcher."""
