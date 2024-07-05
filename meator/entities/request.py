from typing import Generic, TypeVar

RRes = TypeVar("RRes")


class Request(Generic[RRes]): ...
