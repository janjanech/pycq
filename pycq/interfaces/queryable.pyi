from typing import TypeVar, Generic

from .query import Query

T = TypeVar('T')


class Queryable(Generic[T]):
    def __query__(self) -> Query[T]: ...
