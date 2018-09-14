from typing import Generic, Iterable, TypeVar

from .query import Query

T = TypeVar('T')


class IterableQuery(Generic[T], Query[T]):
    def __init__(self, iterable: Iterable[T]):
        self.__iterable = iterable

    def __iter__(self):
        return iter(self.__iterable)

    def to_list(self):
        return list(self.__iterable)
