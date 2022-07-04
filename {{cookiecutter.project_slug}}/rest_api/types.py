import enum
import typing


class StrEnum(str, enum.Enum):
    """
    String type enum

    """

    pass


StrDict = typing.Dict[str, typing.Any]