from typing import Generic, Iterable, TypeVar

from .query import Query

T = TypeVar('T')


class IterableQuery(Generic[T], Query[T]):
    def __init__(self, iterable: Iterable[T]):
        self.__iterable = iterable

    def __iter__(self):
        return iter(self.__iterable)

    def with_number(self):
        return IterableQuery(enumerate(self.__iterable))

    def select(self, selector):
        return IterableQuery(selector(i) for i in self.__iterable)

    def where(self, condition):
        return IterableQuery(i for i in self.__iterable if condition(i))

    def to_list(self):
        return list(self.__iterable)

    def to_set(self):
        return set(self.__iterable)

    def to_tuple(self):
        return tuple(self.__iterable)

    def to_dict(self, key_selector, value_selector=None):
        if value_selector is None:
            return {key_selector(i): i for i in self.__iterable}
        else:
            return {key_selector(i): value_selector(i) for i in self.__iterable}
