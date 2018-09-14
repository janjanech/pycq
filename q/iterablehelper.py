from typing import Generic, TypeVar, Iterable, Iterator

T = TypeVar('T')


class IterableHelper(Generic[T], Iterable[T]):
    def __init__(self, iterator: Iterator[T]):
        self.__iterator = iterator

    def __iter__(self) -> Iterator[T]:
        return self.__iterator
