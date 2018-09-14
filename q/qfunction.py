from typing import Union, TypeVar, Iterable, Iterator, Generic

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


class Q(metaclass=QFunction):
    def __new__(cls, collection: Union[Queryable[T], Iterable[T], Iterator[T]]) -> Query[T]: ...


__ALL__ = ['Q']
