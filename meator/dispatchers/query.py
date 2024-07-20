from meator.dispatchers.base import BaseDispatcherImpl
from meator.interfaces import IQueryDispatcher


class QueryDispatcherImpl(BaseDispatcherImpl, IQueryDispatcher):
    """Query dispatcher."""
