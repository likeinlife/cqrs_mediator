import typing as tp

from meator._constants import _UNSET

T = tp.TypeVar("T")


def get_default_sentinel(value: T, default_value: T) -> T:
    return value if value is not _UNSET else default_value
