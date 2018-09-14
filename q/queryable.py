from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from .query import Query

T = TypeVar('T')


class Queryable(ABC, Generic[T]):
    @abstractmethod
    def __query__(self) -> Query[T]: ...
