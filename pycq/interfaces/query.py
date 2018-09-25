try:
    from abc import ABC
except ImportError:
    from abc import ABCMeta

    ABC = ABCMeta('ABC', (object, ), {})

from abc import abstractmethod


class Query(ABC):
    def __query__(self):
        return self

    @abstractmethod
    def tee(self): pass

    @abstractmethod
    def with_number(self): pass

    @abstractmethod
    def reduce(self, func_or_initializer, func_if_initializer_given=None): pass

    @abstractmethod
    def select(self, selector): pass

    @abstractmethod
    def select_many(self, selector): pass

    @abstractmethod
    def chain(self): pass

    @abstractmethod
    def where(self, condition): pass

    @abstractmethod
    def cast(self, type): pass

    @abstractmethod
    def of_type(self, type): pass

    @abstractmethod
    def distinct(self, key_selector=None): pass

    @abstractmethod
    def union(self, iterable): pass

    @abstractmethod
    def intersect(self, iterable): pass

    @abstractmethod
    def except_(self, iterable): pass

    @abstractmethod
    def distinct_ordered(self, key_selector=None): pass

    @abstractmethod
    def count(self): pass

    @abstractmethod
    def sum(self, selector=None): pass

    @abstractmethod
    def average(self, selector=None): pass

    @abstractmethod
    def min(self, selector=None): pass

    @abstractmethod
    def having_min(self, selector): pass

    @abstractmethod
    def max(self, selector=None): pass

    @abstractmethod
    def having_max(self, selector): pass

    @abstractmethod
    def first(self, condition=None): pass

    @abstractmethod
    def first_or_default(self, default, condition=None): pass

    @abstractmethod
    def last(self, condition=None): pass

    @abstractmethod
    def last_or_default(self, default, condition=None): pass

    @abstractmethod
    def single(self, condition=None): pass

    @abstractmethod
    def single_or_default(self, default, condition=None): pass

    @abstractmethod
    def skip(self, count): pass

    @abstractmethod
    def skip_while(self, condition): pass

    @abstractmethod
    def skip_last(self, count): pass

    @abstractmethod
    def skip_last_having(self, condition): pass

    @abstractmethod
    def take(self, count): pass

    @abstractmethod
    def take_while(self, condition): pass

    @abstractmethod
    def take_last(self, count): pass

    @abstractmethod
    def take_last_having(self, condition): pass

    @abstractmethod
    def any(self, condition=None): pass

    @abstractmethod
    def all(self, condition): pass

    @abstractmethod
    def contains(self, value): pass

    @abstractmethod
    def contains_all(self, iterable): pass

    @abstractmethod
    def contains_any(self, iterable): pass

    @abstractmethod
    def sequence_equal(self, iterable): pass

    @abstractmethod
    def default_if_empty(self, default): pass

    @abstractmethod
    def prepend_all(self, iterable): pass

    @abstractmethod
    def prepend(self, value): pass

    @abstractmethod
    def append_all(self, iterable): pass

    @abstractmethod
    def append(self, value): pass

    @abstractmethod
    def group_by(self, key_selector): pass

    @abstractmethod
    def group_by_ordered(self, key_selector): pass

    @abstractmethod
    def sort_by(self, key_selector): pass

    @abstractmethod
    def sort_by_desc(self, key_selector): pass

    @abstractmethod
    def reverse(self): pass

    @abstractmethod
    def zip(self, other_iterable): pass

    @abstractmethod
    def zip_longest(self, other_iterable, *, fill=None, fill_left=None, fill_right=None): pass

    @abstractmethod
    def inner_join(self, other_iterable, left_key_selector, right_key_selector): pass

    @abstractmethod
    def group_join(self, other_iterable, left_key_selector, right_key_selector): pass

    @abstractmethod
    def to_list(self): pass

    @abstractmethod
    def to_set(self): pass

    @abstractmethod
    def to_frozenset(self): pass

    @abstractmethod
    def to_tuple(self): pass

    @abstractmethod
    def to_dict(self, key_selector, value_selector=None): pass

    @abstractmethod
    def to_deque(self, max_length=None): pass

    @abstractmethod
    def join(self, separator): pass


class SortingQuery(Query):
    @abstractmethod
    def then_by(self, key_selector): pass

    @abstractmethod
    def then_by_desc(self, key_selector): pass
