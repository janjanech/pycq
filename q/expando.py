from typing import no_type_check


@no_type_check
class Expando:
    __ro = False

    def __init__(self, **attrib):
        self.__dict__ = attrib
        self.__ro = True

    def __setattr__(self, key, value):
        if self.__ro:
            raise AttributeError("attribute '{0}' of 'Obj' objects is not writable")
