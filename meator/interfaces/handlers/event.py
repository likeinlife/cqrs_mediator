import typing as tp

from meator.entities import Event

from .request import IHandler

EType = tp.TypeVar("EType", bound=Event)


class IEventHandler(IHandler[EType, None]): ...
