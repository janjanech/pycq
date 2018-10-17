from collections import Iterable, Iterator, namedtuple, Mapping
from itertools import repeat, count, starmap

from pycq.iterable import IterableHelper, IterableQuery
from pycq.interfaces import Queryable


KeyValue = namedtuple('KeyValue', ['key', 'value'])


class QFunction:
    def __init__(self, *args):
        pass

    def __call__(self, collection):
        if isinstance(collection, Queryable):
            return collection.__query__()
        elif isinstance(collection, Mapping):
            return IterableQuery(starmap(KeyValue, collection.items()))
        elif isinstance(collection, Iterable):
            return IterableQuery(collection)
        elif isinstance(collection, Iterator):
            return IterableQuery(IterableHelper(collection))
        else:
            raise TypeError('collection parameter of Q() function has to be Queryable, Iterable, or Iterator')

    def empty(self):
        return self(())

    def count(self, start):
        return self(count(start))

    def range(self, start, count):
        return self(range(start, start + count))

    def repeat(self, element, count=None):
        if count is None:
            return self(repeat(element))
        else:
            return self(repeat(element, count))

    def split(self, string, separator, count=None):
        if count is None:
            return self(string.split(separator))
        else:
            return self(string.split(separator, count))

    def iterate(self, seed, advance_function):
        return self(self.__iterate(seed, advance_function))

    def __iterate(self, seed, advance_function):
        value = seed
        while True:
            yield value
            value = advance_function(value)


Q = QFunction()

__ALL__ = ['Q']
