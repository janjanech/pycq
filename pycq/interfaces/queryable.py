try:
    from abc import ABC
except ImportError:
    from abc import ABCMeta

    ABC = ABCMeta('ABC', (object, ), {})

from abc import abstractmethod


class Queryable(ABC):
    @abstractmethod
    def __query__(self): pass
