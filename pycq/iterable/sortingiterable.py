class SortingComparer:
    def __init__(self, values):
        self.__values = values

    def __lt__(self, other):
        for (value, desc), (other_value, desc) in zip(self.__values, other.__values):
            if value < other_value:
                return not desc
            elif value > other_value:
                return desc

        return False

    def __le__(self, other):
        for (value, desc), (other_value, desc) in zip(self.__values, other.__values):
            if value < other_value:
                return not desc
            elif value > other_value:
                return desc

        return True

    def __eq__(self, other):
        for (value, desc), (other_value, desc) in zip(self.__values, other.__values):
            if value != other_value:
                return False

        return True

    def __ne__(self, other):
        for (value, desc), (other_value, desc) in zip(self.__values, other.__values):
            if value != other_value:
                return True

        return False

    def __gt__(self, other):
        for (value, desc), (other_value, desc) in zip(self.__values, other.__values):
            if value > other_value:
                return not desc
            elif value < other_value:
                return desc

        return False

    def __ge__(self, other):
        for (value, desc), (other_value, desc) in zip(self.__values, other.__values):
            if value > other_value:
                return not desc
            elif value < other_value:
                return desc

        return True


class SortingKey:
    def __init__(self, key_selector, desc=False):
        if isinstance(key_selector, tuple):
            self.__key_parts = key_selector
        else:
            self.__key_parts = ((key_selector, desc), )

    def resolve(self):
        if not any(x[1] for x in self.__key_parts):
            return SortingKeyAllAsc(key_selector for key_selector, desc in self.__key_parts)
        return self

    def __call__(self, item):
        return SortingComparer([(key_selector(item), desc) for key_selector, desc in self.__key_parts])

    def add_key(self, key_selector, desc=False):
        return SortingKey(self.__key_parts + ((key_selector, desc), ))


class SortingKeyAllAsc:
    def __init__(self, key_selectors):
        self.__key_selectors = tuple(key_selectors)

    def __call__(self, item):
        return tuple(key_selector(item) for key_selector in self.__key_selectors)


class SortingIterable:
    def __init__(self, iterable, key_selector, desc=False):
        self.__iterable = iterable

        if isinstance(key_selector, SortingKey):
            self.__key = key_selector
        else:
            self.__key = SortingKey(key_selector, desc)

    def __iter__(self):
        return iter(sorted(self.__iterable, key=self.__key.resolve()))

    def add_key(self, key_selector, desc=False):
        return SortingIterable(self.__iterable, self.__key.add_key(key_selector, desc))
