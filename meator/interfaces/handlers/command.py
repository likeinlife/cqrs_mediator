import typing as tp

from meator.entities import Command

from .request import Handler

HRes = tp.TypeVar("HRes")
CType = tp.TypeVar("CType", bound=Command)


class CommandHandler(Handler[CType, HRes]): ...
