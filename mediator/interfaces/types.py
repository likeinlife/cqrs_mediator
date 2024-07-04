import typing as tp

if tp.TYPE_CHECKING:
    from mediator.entities import Request
    from mediator.interfaces.handlers import IHandler
    from mediator.interfaces.middleware import IMiddleware

T = tp.TypeVar("T")

CallNextType: tp.TypeAlias = "IHandler[Request, T] | IMiddleware"
