try:
    from abc import ABC
except ImportError:
    from abc import ABCMeta

    class ABC(metaclass=ABCMeta): pass

from abc import abstractmethod
from typing import Generic, List, TypeVar, Iterable, overload, Callable, Dict, Set, Tuple, Type

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


class NumberedItem(ABC, Generic[T]):
    @property
    @abstractmethod
    def no(self) -> int: ...

    @property
    @abstractmethod
    def item(self) -> T: ...


class GroupedItems(ABC, Generic[TKey, T]):
    @property
    @abstractmethod
    def key(self) -> TKey: ...

    @property
    @abstractmethod
    def items(self) -> "Query[T]": ...


class Query(ABC, Generic[T], Iterable[T]):
    def __query__(self) -> "Query[T]":
        return self

    @abstractmethod
    def with_number(self) -> "Query[NumberedItem[T]]": ...

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
    def cast(self, type: Type[TValue]) -> "Query[TValue]": ...

    @abstractmethod
    def of_type(self, type: Type[TValue]) -> "Query[TValue]": ...

    @abstractmethod
    def count(self) -> int: ...

    @overload
    def sum(self) -> T: ...

    @overload
    def sum(self, selector: Callable[[T], TValue]) -> TValue: ...

    @abstractmethod
    def sum(self, selector=None): ...

    @overload
    def average(self) -> TValue: ...

    @overload
    def average(self, selector: Callable[[T], TValue]) -> TValue: ...

    @abstractmethod
    def average(self, selector=None): ...

    @overload
    def min(self) -> T: ...

    @overload
    def min(self, selector: Callable[[T], TValue]) -> TValue: ...

    @abstractmethod
    def min(self, selector=None): ...

    @abstractmethod
    def having_min(self, selector: Callable[[T], TValue]) -> "Query[T]": ...

    @overload
    def max(self) -> T: ...

    @overload
    def max(self, selector: Callable[[T], TValue]) -> TValue: ...

    @abstractmethod
    def max(self, selector=None): ...

    @abstractmethod
    def having_max(self, selector: Callable[[T], TValue]) -> "Query[T]": ...

    @overload
    def first(self) -> T: ...

    @overload
    def first(self, condition: Callable[[T], bool]) -> T: ...

    @abstractmethod
    def first(self, condition=None): ...

    @overload
    def first_or_default(self, default: T) -> T: ...

    @overload
    def first_or_default(self, default: T, condition: Callable[[T], bool]) -> T: ...

    @abstractmethod
    def first_or_default(self, default, condition=None): ...

    @overload
    def last(self) -> T: ...

    @overload
    def last(self, condition: Callable[[T], bool]) -> T: ...

    @abstractmethod
    def last(self, condition=None): ...

    @overload
    def last_or_default(self, default: T) -> T: ...

    @overload
    def last_or_default(self, default: T, condition: Callable[[T], bool]) -> T: ...

    @abstractmethod
    def last_or_default(self, default, condition=None): ...

    @abstractmethod
    def any(self, condition: Callable[[T], bool] = None) -> bool: ...

    @abstractmethod
    def all(self, condition: Callable[[T], bool]) -> bool: ...

    @abstractmethod
    def contains(self, value: T) -> bool: ...

    @abstractmethod
    def contains_all(self, iterable: Iterable[T]) -> bool: ...

    @abstractmethod
    def contains_any(self, iterable: Iterable[T]) -> bool: ...

    @abstractmethod
    def sequence_equal(self, iterable: Iterable[T]) -> bool: ...

    @abstractmethod
    def default_if_empty(self, default: T) -> "Query[T]": ...

    @abstractmethod
    def prepend_all(self, iterable: Iterable[T]) -> "Query[T]": ...

    @abstractmethod
    def prepend(self, value: T) -> "Query[T]": ...

    @abstractmethod
    def append_all(self, iterable: Iterable[T]) -> "Query[T]": ...

    @abstractmethod
    def append(self, value: T) -> "Query[T]": ...

    @abstractmethod
    def group_by(self, key_selector: Callable[[T], TKey]) -> "Query[GroupedItems[TKey, T]]": ...

    @abstractmethod
    def group_by_ordered(self, key_selector: Callable[[T], TKey]) -> "Query[GroupedItems[TKey, T]]": ...

    @abstractmethod
    def reverse(self) -> "Query[T]": ...

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
