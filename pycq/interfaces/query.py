try:
    from abc import ABC
except ImportError:
    from abc import ABCMeta


    class ABC(metaclass=ABCMeta):
        pass

from abc import abstractmethod
from typing import Generic, List, TypeVar, Iterable, overload, Callable, Dict, Set, Tuple, Type, AnyStr, FrozenSet

T = TypeVar('T')
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
TOther = TypeVar('TOther')
TItem = TypeVar('TItem')


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


class ZippedItems(ABC, Generic[T, TOther]):
    @property
    @abstractmethod
    def left(self) -> T: ...

    @property
    @abstractmethod
    def right(self) -> TOther: ...


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
    def chain(self: "Query[Iterable[TItem]]") -> "Query[TItem]": ...

    @abstractmethod
    def where(self, condition: Callable[[T], bool]) -> "Query[T]": ...

    @abstractmethod
    def cast(self, type: Type[TValue]) -> "Query[TValue]": ...

    @abstractmethod
    def of_type(self, type: Type[TValue]) -> "Query[TValue]": ...

    @abstractmethod
    def distinct(self, key_selector: Callable[[T], bool] = None) -> "Query[T]": ...

    @abstractmethod
    def union(self, iterable: Iterable[T]) -> "Query[T]": ...

    @abstractmethod
    def intersect(self, iterable: Iterable[T]) -> "Query[T]": ...

    @abstractmethod
    def except_(self, iterable: Iterable[T]) -> "Query[T]": ...

    @abstractmethod
    def distinct_ordered(self, key_selector: Callable[[T], bool] = None) -> "Query[T]": ...

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
    def skip(self, count: int) -> "Query[T]": ...

    @abstractmethod
    def skip_while(self, condition: Callable[[T], bool]) -> "Query[T]": ...

    @abstractmethod
    def take(self, count: int) -> "Query[T]": ...

    @abstractmethod
    def take_while(self, condition: Callable[[T], bool]) -> "Query[T]": ...

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
    def sort_by(self, key_selector: Callable[[T], TKey]) -> "SortingQuery[T]": ...

    @abstractmethod
    def sort_by_desc(self, key_selector: Callable[[T], TKey]) -> "SortingQuery[T]": ...

    @abstractmethod
    def reverse(self) -> "Query[T]": ...

    @abstractmethod
    def zip(self, other_iterable: Iterable[TOther]) -> "Query[ZippedItems[T, TOther]]": ...

    @overload
    def zip_longest(self, other_iterable: Iterable[TOther], *, fill_left: T = None, fill_right: TOther = None)\
            -> "Query[ZippedItems[T, TOther]]": ...

    @overload
    def zip_longest(self, other_iterable: Iterable[T], *, fill: T = None)\
            -> "Query[ZippedItems[T, T]]": ...

    @abstractmethod
    def zip_longest(self, other_iterable, *, fill=None, fill_left=None, fill_right=None): ...

    @abstractmethod
    def to_list(self) -> List[T]: ...

    @abstractmethod
    def to_set(self) -> Set[T]: ...

    @abstractmethod
    def to_frozenset(self) -> FrozenSet[T]: ...

    @abstractmethod
    def to_tuple(self) -> Tuple[T, ...]: ...

    @overload
    def to_dict(self, key_selector: Callable[[T], TKey]) -> Dict[TKey, T]: ...

    @overload
    def to_dict(self, key_selector: Callable[[T], TKey], value_selector: Callable[[T], TValue]) -> Dict[TKey, TValue]: ...

    @abstractmethod
    def to_dict(self, key_selector, value_selector=None): ...

    @abstractmethod
    def join(self: "Query[AnyStr]", separator: AnyStr) -> AnyStr: ...


class SortingQuery(Generic[T], Query[T]):
    @abstractmethod
    def then_by(self, key_selector: Callable[[T], TKey]) -> "SortingQuery[T]": ...

    @abstractmethod
    def then_by_desc(self, key_selector: Callable[[T], TKey]) -> "SortingQuery[T]": ...