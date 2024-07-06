import typing as tp

from meator.entities import Query

from .request import IHandler

HRes = tp.TypeVar("HRes")
QType = tp.TypeVar("QType", bound=Query)


class IQueryHandler(IHandler[QType, HRes]): ...
