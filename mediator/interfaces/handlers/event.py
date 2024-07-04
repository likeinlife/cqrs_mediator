import typing as tp

from mediator.entities import Event

from .request import IHandler

HRes = tp.TypeVar("HRes")
EType = tp.TypeVar("EType", bound=Event)


class IEventHandler(IHandler[EType, HRes]): ...
