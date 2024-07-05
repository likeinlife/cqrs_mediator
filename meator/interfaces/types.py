import typing as tp

if tp.TYPE_CHECKING:
    from meator.entities import Request
    from meator.interfaces.handlers import IHandler
    from meator.interfaces.middleware import IMiddleware

T = tp.TypeVar("T")

CallNextType: tp.TypeAlias = "IHandler[Request, T] | IMiddleware"
