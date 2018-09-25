class Expando:
    __ro = False

    def __init__(self, **attrib):
        self.__dict__ = attrib
        self.__ro = True

    def __setattr__(self, key, value):
        if self.__ro:
            raise AttributeError("attribute '{0}' of 'Obj' objects is not writable")
        super().__setattr__(key, value)

    def __str__(self):
        return "Expando({0})".format(
            ", ".join(
                "{0}={1!r}".format(name, value) for name, value in self.__dict__.items() if not name.startswith('_')
            )
        )

    __repr__ = __str__
