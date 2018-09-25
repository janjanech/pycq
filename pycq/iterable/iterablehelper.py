class IterableHelper:
    def __init__(self, iterator):
        self.__iterator = iterator

    def __iter__(self):
        return self.__iterator
