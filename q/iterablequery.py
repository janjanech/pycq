from functools import reduce
from typing import Generic, Iterable, TypeVar, Sized

from .query import Query

T = TypeVar('T')


class IterableQuery(Generic[T], Query[T]):
    def __init__(self, iterable: Iterable[T]):
        self.__iterable = iterable

    def __iter__(self):
        return iter(self.__iterable)

    def with_number(self):
        return IterableQuery(enumerate(self.__iterable))

    def reduce(self, func_or_initializer, func_if_initializer_given=None):
        if func_if_initializer_given is not None:
            return reduce(func_if_initializer_given, self.__iterable, func_or_initializer)
        else:
            return reduce(func_or_initializer, self.__iterable)

    def select(self, selector):
        return IterableQuery(selector(i) for i in self.__iterable)

    def where(self, condition):
        return IterableQuery(i for i in self.__iterable if condition(i))

    def count(self):
        if isinstance(self.__iterable, Sized):
            return len(self.__iterable)
        else:
            cnt = 0
            for i in self.__iterable:
                cnt += 1
            return cnt

    def any(self, condition=None):
        if condition is None:
            for i in self.__iterable:
                return True
            return False
        else:
            return any(condition(i) for i in self.__iterable)

    def all(self, condition):
        return all(condition(i) for i in self.__iterable)

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

    def join(self, separator):
        return separator.join(self.__iterable)
