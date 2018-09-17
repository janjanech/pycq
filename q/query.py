from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, Iterable, overload, Callable, Dict, Set, Tuple

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


class Query(ABC, Generic[T], Iterable[T]):
    def __query__(self) -> "Query[T]":
        return self

    @abstractmethod
    def with_number(self) -> "Query[Tuple[int, T]]": ...

    @overload
    def reduce(self, func: Callable[[T, T], T]) -> T: ...

    @overload
    def reduce(self, initializer: TValue, func: Callable[[TValue, T], TValue]) -> TValue: ...

    @abstractmethod
    def reduce(self, func_or_initializer, func_if_initializer_given=None): ...

    @abstractmethod
    def select(self, selector: Callable[[T], TValue]) -> "Query[TValue]": ...

    @abstractmethod
    def select_many(self, selector: Callable[[T], Iterable[TValue]]) -> "Query[TValue]": ...

    @abstractmethod
    def where(self, condition: Callable[[T], bool]) -> "Query[T]": ...

    @abstractmethod
    def count(self) -> int: ...

    @abstractmethod
    def any(self, condition: Callable[[T], bool] = None) -> bool: ...

    @abstractmethod
    def all(self, condition: Callable[[T], bool]) -> bool: ...

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
    
    @abstractmethod
    def join(self, separator: str) -> str: ...
