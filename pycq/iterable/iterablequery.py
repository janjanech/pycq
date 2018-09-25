from collections import namedtuple, deque
from functools import reduce
from itertools import chain, zip_longest, starmap, groupby, islice, dropwhile, takewhile, tee
from typing import Generic, Iterable, TypeVar, Sized

from pycq.interfaces import SortingQuery
from .sortingiterable import SortingIterable

T = TypeVar('T')

NumberedItem = namedtuple('NumberedItem', ['no', 'item'])
GroupedItems = namedtuple('GroupedItems', ['key', 'items'])
ZippedItems = namedtuple('ZippedItems', ['left', 'right'])
JoinedItems = namedtuple('JoinedItems', ['key', 'left', 'right'])
GroupJoinedItems = namedtuple('GroupJoinedItems', ['key', 'left_items', 'right_items'])


class IterableQuery(Generic[T], SortingQuery[T]):
    def __init__(self, iterable: Iterable[T]):
        self.__iterable = iterable

    def __iter__(self):
        return iter(self.__iterable)

    def tee(self):
        self.__iterable, ret = tee(self.__iterable)
        return IterableQuery(ret)

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

    def chain(self):
        return IterableQuery(chain.from_iterable(self.__iterable))

    def where(self, condition):
        return IterableQuery(i for i in self.__iterable if condition(i))

    def cast(self, type):
        return IterableQuery(type(i) for i in self.__iterable)

    def of_type(self, type):
        # noinspection PyTypeHints
        return IterableQuery(i for i in self.__iterable if isinstance(i, type))

    def distinct(self, key_selector=None):
        if key_selector is None:
            return IterableQuery(set(self.__iterable))
        else:
            return IterableQuery(self.__distinct(key_selector))

    def __distinct(self, key_selector):
        keys = set()
        for i in self.__iterable:
            key = key_selector(i)
            if key not in keys:
                yield i
                keys.add(key)

    def distinct_ordered(self, key_selector=None):
        if key_selector is None:
            return IterableQuery(self.__distinct_ordered())
        else:
            return IterableQuery(self.__distinct_ordered_with_key_selector(key_selector))

    def __distinct_ordered(self):
        last_item = object()
        for i in self.__iterable:
            if last_item != i:
                last_item = i
                yield i

    def __distinct_ordered_with_key_selector(self, key_selector):
        last_key = object()
        for i in self.__iterable:
            key = key_selector(i)
            if last_key != key:
                last_key = key
                yield i

    def union(self, iterable):
        return IterableQuery(self.__union(iterable))

    def __union(self, iterable):
        union = set()

        for i in self.__iterable:
            if i not in union:
                union.add(i)
                yield i

        for i in iterable:
            if i not in union:
                union.add(i)
                yield i

    def intersect(self, iterable):
        return IterableQuery(self.__intersect(iterable))

    def __intersect(self, iterable):
        interesction = set(iterable)

        for i in self.__iterable:
            if i in interesction:
                interesction.remove(i)
                yield i

    def except_(self, iterable):
        return IterableQuery(self.__except(iterable))

    def __except(self, iterable):
        difference = set(iterable)

        for i in self.__iterable:
            if i not in difference:
                difference.add(i)
                yield i

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

    def skip_last(self, count):
        return IterableQuery(self.__skip_last(count))

    def __skip_last(self, count):
        ret = deque()
        for i in self.__iterable:
            ret.append(i)
            if len(ret) > count:
                yield ret.popleft()

    def skip_last_having(self, condition):
        return IterableQuery(self.__skip_last_having(condition))

    def __skip_last_having(self, condition):
        ret = deque()
        for i in self.__iterable:
            if condition(i):
                ret.append(i)
            else:
                while ret:
                    yield ret.popleft()
                yield i

    def take(self, count):
        return IterableQuery(islice(self.__iterable, count))

    def take_last(self, count):
        return IterableQuery(deque(self.__iterable, count))

    def take_while(self, condition):
        return IterableQuery(takewhile(condition, self.__iterable))

    def take_last_having(self, condition):
        return IterableQuery(self.__take_last_having(condition))

    def __take_last_having(self, condition):
        ret = deque()
        for i in self.__iterable:
            if condition(i):
                ret.append(i)
            else:
                ret.clear()

        while ret:
            yield ret.popleft()

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

    def sort_by(self, key_selector):
        sorting_iterable = SortingIterable(self.__iterable, key_selector, False)
        return IterableQuery(sorting_iterable)

    def sort_by_desc(self, key_selector):
        sorting_iterable = SortingIterable(self.__iterable, key_selector, True)
        return IterableQuery(sorting_iterable)

    def then_by(self, key_selector):
        if not isinstance(self.__iterable, SortingIterable):
            raise TypeError("then_by cannot be used without preceding sort_by")
        sorting_iterable = self.__iterable.add_key(key_selector, False)
        return IterableQuery(sorting_iterable)

    def then_by_desc(self, key_selector):
        if not isinstance(self.__iterable, SortingIterable):
            raise TypeError("then_by cannot be used without preceding sort_by")
        sorting_iterable = self.__iterable.add_key(key_selector, False)
        return IterableQuery(sorting_iterable)

    def zip(self, other_iterable):
        return IterableQuery(starmap(ZippedItems, zip(self.__iterable, other_iterable)))

    def zip_longest(self, other_iterable, *, fill=None, fill_left=None, fill_right=None):
        if fill_left is None and fill_right is None:
            return IterableQuery(starmap(ZippedItems, zip_longest(self.__iterable, other_iterable, fillvalue=fill)))
        elif fill_left is fill_right:
            return IterableQuery(starmap(ZippedItems, zip_longest(self.__iterable, other_iterable, fillvalue=fill_left)))
        else:
            return IterableQuery(self.__zip_longest(other_iterable, fill_left, fill_right))

    def __zip_longest(self, other_iterable, fill_left, fill_right):
        marker = object()

        for left_item, right_item in zip_longest(self.__iterable, other_iterable, fillvalue=marker):
            if left_item is marker:
                left_item = fill_left
            if right_item is marker:
                right_item = fill_right

            yield ZippedItems(left_item, right_item)

    def inner_join(self, other_iterable, left_key_selector, right_key_selector):
        return IterableQuery(self.__inner_join(other_iterable, left_key_selector, right_key_selector))

    def __inner_join(self, other_iterable, left_key_selector, right_key_selector):
        index = {}
        for item in other_iterable:
            key = right_key_selector(item)
            index.setdefault(key, []).append(item)

        for item in self.__iterable:
            key = left_key_selector(item)
            for inner_item in index.get(key, ()):
                yield JoinedItems(key, item, inner_item)

    def group_join(self, other_iterable, left_key_selector, right_key_selector):
        return IterableQuery(self.__grouped_join(other_iterable, left_key_selector, right_key_selector))

    def __grouped_join(self, other_iterable, left_key_selector, right_key_selector):
        left_index = {}
        for item in self.__iterable:
            key = left_key_selector(item)
            left_index.setdefault(key, []).append(item)

        right_index = {}
        for item in other_iterable:
            key = right_key_selector(item)
            right_index.setdefault(key, []).append(item)

        for key, left_items in left_index.items():
            yield GroupJoinedItems(key, IterableQuery(left_items), IterableQuery(right_index.get(key, ())))

        for key, right_items in right_index.items():
            if key not in left_index:
                yield GroupJoinedItems(key, IterableQuery(()), IterableQuery(right_items))

    def to_list(self):
        return list(self.__iterable)

    def to_set(self):
        return set(self.__iterable)

    def to_frozenset(self):
        return frozenset(self.__iterable)

    def to_tuple(self):
        return tuple(self.__iterable)

    def to_dict(self, key_selector, value_selector=None):
        if value_selector is None:
            return {key_selector(i): i for i in self.__iterable}
        else:
            return {key_selector(i): value_selector(i) for i in self.__iterable}

    def to_deque(self, max_length=None):
        return deque(self.__iterable, max_length)

    def join(self, separator):
        return separator.join(self.__iterable)
