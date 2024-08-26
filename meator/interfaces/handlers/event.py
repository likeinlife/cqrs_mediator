import typing as tp

from meator.entities import Event

from .request import Handler

EType = tp.TypeVar("EType", bound=Event)


class EventHandler(Handler[EType, None]): ...
