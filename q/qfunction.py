from itertools import repeat, count
from typing import Union, TypeVar, Iterable, Iterator, Optional, Any

from .iterablehelper import IterableHelper
from .query import Query
from .iterablequery import IterableQuery
from .queryable import Queryable

T = TypeVar('T')


class QFunction:
    def __init__(self, *args):
        pass

    def __call__(self, collection: Union[Queryable[T], Iterable[T], Iterator[T]]) -> Query[T]:
        if isinstance(collection, Queryable):
            return collection.__query__()
        elif isinstance(collection, Iterable):
            return IterableQuery(collection)
        elif isinstance(collection, Iterator):
            return IterableQuery(IterableHelper(collection))
        else:
            raise TypeError('collection parameter of Q() function has to be Queryable, Iterable, or Iterator')

    def empty(self) -> Query[Any]:
        return self(())

    def count(self, start: int) -> Query[int]:
        return self(count(start))

    def range(self, start: int, count: int) -> Query[int]:
        return self(range(start, start + count))

    def repeat(self, element: T, count: Optional[int] = None) -> Query[T]:
        if count is None:
            return self(repeat(element))
        else:
            return self(repeat(element, count))


class Q(metaclass=QFunction):
    def __new__(cls, collection: Union[Queryable[T], Iterable[T], Iterator[T]]) -> Query[T]: ...

    @staticmethod
    def empty() -> Query[Any]: ...

    @staticmethod
    def count(start: int) -> Query[int]: ...

    @staticmethod
    def range(start: int, count: int) -> Query[int]: ...

    @staticmethod
    def repeat(element: T, count: Optional[int] = None) -> Query[T]: ...


__ALL__ = ['Q']
