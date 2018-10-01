try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from .namespace import FallbackNamespace as Namespace


class Expando(Namespace):
    def __with__(self, **attrib):
        new_attrib = self.__dict__.copy()
        new_attrib.update(attrib)
        return Expando(**new_attrib)

    def __setattr__(self, key, value):
        raise AttributeError("attribute '{0}' of 'Expando' objects is not writable".format(key))

    def __delattr__(self, key):
        raise AttributeError("attribute '{0}' of 'Expando' objects is not writable".format(key))

    def __str__(self):
        return "Expando({0})".format(
            ", ".join(
                "{0}={1!r}".format(name, value) for name, value in self.__dict__.items() if not name.startswith('_')
            )
        )

    __repr__ = __str__
