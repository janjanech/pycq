from typing import Union, TypeVar, Iterable, Iterator, Optional, Any, AnyStr, Callable

from pycq.interfaces import Query, Queryable

T = TypeVar('T')

class Q:
    def __new__(cls, collection: Union[Queryable[T], Iterable[T], Iterator[T]]) -> Query[T]: ...

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
