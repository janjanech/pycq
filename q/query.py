from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, Iterable, Iterator

T = TypeVar('T')


class Query(ABC, Generic[T], Iterable[T]):
    def __query__(self) -> "Query[T]":
        return self

    @abstractmethod
    def to_list(self) -> List[T]: ...
