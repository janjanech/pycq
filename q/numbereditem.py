from typing import Generic, TypeVar

T = TypeVar('T')


# noinspection PyCompatibility
class NumberedItem(Generic[T]):
    no: int
    item: T
