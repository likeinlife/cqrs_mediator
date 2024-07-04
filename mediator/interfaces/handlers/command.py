import typing as tp

from mediator.entities import Command

from .request import IHandler

HRes = tp.TypeVar("HRes")
CType = tp.TypeVar("CType", bound=Command)


class ICommandHandler(IHandler[CType, HRes]): ...
