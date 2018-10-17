from typing import TypeVar, Iterable, Iterator, Optional, Any, AnyStr, Callable, overload, Mapping, Generic

from pycq.interfaces import Query, Queryable

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


class KeyValue(Generic[TKey, TValue]):
    @property
    def key(self) -> TKey: ...

    @property
    def value(self) -> TValue: ...


class Q:
    @overload
    def __new__(cls, collection: Queryable[T]) -> Query[T]: ...

    @overload
    def __new__(cls, collection: Mapping[TKey, TValue]) -> Query[KeyValue[TKey, TValue]]: ...

    @overload
    def __new__(cls, collection: Iterable[T]) -> Query[T]: ...

    @overload
    def __new__(cls, collection: Iterator[T]) -> Query[T]: ...

    @staticmethod
    def empty() -> Query[Any]: ...

    @staticmethod
    def count(start: int) -> Query[int]: ...

    @staticmethod
    def range(start: int, count: int) -> Query[int]: ...

    @staticmethod
    def repeat(element: T, count: Optional[int] = None) -> Query[T]: ...
    
    @staticmethod
    def split(string: AnyStr, separator: Optional[AnyStr], count: AnyStr = None) -> Query[AnyStr]: ...
    
    @staticmethod
    def iterate(seed: T, advance_function: Callable[[T], T]) -> Query[T]: ...
