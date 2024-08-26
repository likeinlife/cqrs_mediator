import typing as tp

from meator.entities import Query

from .request import Handler

HRes = tp.TypeVar("HRes")
QType = tp.TypeVar("QType", bound=Query)


class QueryHandler(Handler[QType, HRes]): ...
