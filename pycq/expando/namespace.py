class FallbackNamespace:
    def __init__(self, **attrib):
        self.__dict__.update(**attrib)
