from dataclasses import dataclass


@dataclass(eq=False)
class BaseError(Exception):
    @property
    def message(self) -> str:
        return "Base error"

    def __str__(self) -> str:
        return self.message
