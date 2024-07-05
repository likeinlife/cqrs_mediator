import typing as tp

from meator.entities import Query

from .request import IHandler

HRes = tp.TypeVar("HRes")


class IQueryHandler(IHandler[Query, HRes]): ...
