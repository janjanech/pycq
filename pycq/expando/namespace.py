class FallbackNamespace(dict):
    __getattr__ = dict.__getitem__
