from collections import namedtuple
from functools import reduce
from itertools import chain, zip_longest, starmap, groupby, islice, dropwhile, takewhile
from typing import Generic, Iterable, TypeVar, Sized

from .query import Query

T = TypeVar('T')

NumberedItem = namedtuple('NumberedItem', ['no', 'item'])
GroupedItems = namedtuple('GroupedItems', ['key', 'items'])


class IterableQuery(Generic[T], Query[T]):
    def __init__(self, iterable: Iterable[T]):
        self.__iterable = iterable

    def __iter__(self):
        return iter(self.__iterable)

    def with_number(self):
        return IterableQuery(starmap(NumberedItem, enumerate(self.__iterable)))

    def reduce(self, func_or_initializer, func_if_initializer_given=None):
        if func_if_initializer_given is not None:
            return reduce(func_if_initializer_given, self.__iterable, func_or_initializer)
        else:
            return reduce(func_or_initializer, self.__iterable)

    def select(self, selector):
        return IterableQuery(selector(i) for i in self.__iterable)

    def select_many(self, selector):
        return IterableQuery(chain.from_iterable(selector(i) for i in self.__iterable))

    def where(self, condition):
        return IterableQuery(i for i in self.__iterable if condition(i))

    def cast(self, type):
        return IterableQuery(type(i) for i in self.__iterable)

    def of_type(self, type):
        # noinspection PyTypeHints
        return IterableQuery(i for i in self.__iterable if isinstance(i, type))

    def count(self):
        if isinstance(self.__iterable, Sized):
            return len(self.__iterable)
        else:
            cnt = 0
            for i in self.__iterable:
                cnt += 1
            return cnt

    def sum(self, selector=None):
        if selector is None:
            return sum(self.__iterable)
        else:
            return sum(selector(i) for i in self.__iterable)

    def average(self, selector=None):
        current_sum = 0
        current_count = 0

        if selector is None:
            for item in self.__iterable:
                current_sum += item
                current_count += 1
        else:
            for item in self.__iterable:
                current_sum += selector(item)
                current_count += 1

        return current_sum / current_count

    def min(self, selector=None):
        if selector is None:
            return min(self.__iterable)
        else:
            return min(selector(i) for i in self.__iterable)

    def having_min(self, selector):
        min_value = None
        min_items = None

        for item in self.__iterable:
            value = selector(item)
            if min_value is None or value < min_value:
                min_items = [item]
                min_value = value
            elif min_value == value:
                min_items.append(item)

        if min_items is None:
            raise ValueError("sequence was empty")

        return IterableQuery(min_items)

    def max(self, selector=None):
        if selector is None:
            return max(self.__iterable)
        else:
            return max(selector(i) for i in self.__iterable)

    def having_max(self, selector):
        max_value = None
        max_items = None

        for item in self.__iterable:
            value = selector(item)
            if max_value is None or value > max_value:
                max_items = [item]
                max_value = value
            elif max_value == value:
                max_items.append(item)

        if max_items is None:
            raise ValueError("sequence was empty")

        return IterableQuery(max_items)

    def first(self, condition=None):
        for i in self.__iterable:
            if condition is None or condition(i):
                return i

        raise ValueError("sequence was empty")

    def first_or_default(self, default, condition=None):
        for i in self.__iterable:
            if condition is None or condition(i):
                return i

        return default

    def last(self, condition=None):
        last_value = marker = object()

        for i in self.__iterable:
            if condition is None or condition(i):
                last_value = i

        if last_value is marker:
            raise ValueError("sequence was empty")

        return last_value

    def last_or_default(self, default, condition=None):
        last_value = default

        for i in self.__iterable:
            if condition is None or condition(i):
                last_value = i

        return last_value

    def skip(self, count):
        return IterableQuery(islice(self.__iterable, count, None))

    def skip_while(self, condition):
        return IterableQuery(dropwhile(condition, self.__iterable))

    def take(self, count):
        return IterableQuery(islice(self.__iterable, count))

    def take_while(self, condition):
        return IterableQuery(takewhile(condition, self.__iterable))

    def any(self, condition=None):
        if condition is None:
            for i in self.__iterable:
                return True
            return False
        else:
            return any(condition(i) for i in self.__iterable)

    def all(self, condition):
        return all(condition(i) for i in self.__iterable)

    def contains(self, value):
        for i in self.__iterable:
            if i == value:
                return True
        return False

    def contains_all(self, iterable):
        values = set(iterable)
        for i in self.__iterable:
            if i in values:
                values.remove(i)
                if not values:
                    return True
        return False

    def contains_any(self, iterable):
        values = frozenset(iterable)
        for i in self.__iterable:
            if i in values:
                return True
        return False

    def sequence_equal(self, iterable):
        for a, b in zip_longest(self.__iterable, iterable, fillvalue=object()):
            if a != b:
                return False
        return True

    def default_if_empty(self, default):
        return IterableQuery(self.__exec_default_if_empty(default))

    def __exec_default_if_empty(self, default):
        it = iter(self.__iterable)
        has_value = False
        while True:
            try:
                yield next(it)
                has_value = True
            except StopIteration:
                break
        if not has_value:
            yield default

    def prepend_all(self, iterable):
        return IterableQuery(chain(iterable, self.__iterable))

    def prepend(self, value):
        return IterableQuery(chain((value, ), self.__iterable))

    def append_all(self, iterable):
        return IterableQuery(chain(self.__iterable, iterable))

    def append(self, value):
        return IterableQuery(chain(self.__iterable, (value, )))

    def group_by(self, key_selector):
        result = {}
        for item in self.__iterable:
            result.setdefault(key_selector(item), []).append(item)

        return IterableQuery(GroupedItems(key, IterableQuery(items)) for key, items in result.items())

    def group_by_ordered(self, key_selector):
        result = groupby(self.__iterable, key_selector)

        return IterableQuery(GroupedItems(key, IterableQuery(items)) for key, items in result)

    def reverse(self):
        if hasattr(self.__iterable, '__reversed__'):  # ABC Reversible is not available till python 3.6
            return IterableQuery(reversed(self.__iterable))
        else:
            return IterableQuery(reversed(list(self.__iterable)))

    def to_list(self):
        return list(self.__iterable)

    def to_set(self):
        return set(self.__iterable)

    def to_tuple(self):
        return tuple(self.__iterable)

    def to_dict(self, key_selector, value_selector=None):
        if value_selector is None:
            return {key_selector(i): i for i in self.__iterable}
        else:
            return {key_selector(i): value_selector(i) for i in self.__iterable}

    def join(self, separator):
        return separator.join(self.__iterable)
