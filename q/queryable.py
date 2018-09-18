try:
    from abc import ABC
except ImportError:
    from abc import ABCMeta

    class ABC(metaclass=ABCMeta): pass

from abc import abstractmethod
from typing import TypeVar, Generic

from .query import Query

T = TypeVar('T')


class Queryable(ABC, Generic[T]):
    @abstractmethod
    def __query__(self) -> Query[T]: ...
