from typing import no_type_check


@no_type_check
class Expando:
    def __init__(self, **attrib): ...
    def __with__(self, **attrib) -> Expando: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
