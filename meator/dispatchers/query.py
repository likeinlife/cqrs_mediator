from meator.dispatchers.base import DispatcherImpl
from meator.interfaces import QueryDispatcher


class QueryDispatcherImpl(DispatcherImpl, QueryDispatcher):
    """Query dispatcher."""
