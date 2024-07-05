from dataclasses import dataclass

from meator.entities import Request
from meator.errors import BaseError


class DispatcherError(BaseError): ...


@dataclass(eq=False)
class HandlerNotFoundError(DispatcherError):
    request_type: type[Request]

    @property
    def message(self) -> str:
        return f"Request handler for {self.request_type.__name__} request is not registered"
