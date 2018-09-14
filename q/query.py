from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, Iterable, overload, Callable, Dict, Set, Tuple

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


class Query(ABC, Generic[T], Iterable[T]):
    def __query__(self) -> "Query[T]":
        return self

    @abstractmethod
    def where(self, condition: Callable[[T], bool]) -> "Query[T]": ...

    @abstractmethod
    def to_list(self) -> List[T]: ...

    @abstractmethod
    def to_set(self) -> Set[T]: ...

    @abstractmethod
    def to_tuple(self) -> Tuple[T, ...]: ...

    @overload
    def to_dict(self, key_selector: Callable[[T], TKey]) -> Dict[TKey, T]: ...

    @overload
    def to_dict(self, key_selector: Callable[[T], TKey], value_selector: Callable[[T], TValue]) -> Dict[TKey, TValue]: ...

    @abstractmethod
    def to_dict(self, key_selector, value_selector=None): ...
