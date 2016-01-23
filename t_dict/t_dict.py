# -*- coding: utf-8 -*-

from copy import deepcopy
from jsonpointer import resolve_pointer, set_pointer

#py2-py3
try:
    from collections import MutableMapping
except ImportError:
    from collections.abc import MutableMapping


class TDict(MutableMapping):

    def __init__(self, d=None):
        if d is None:
            self.__d = {}
        elif isinstance(d, self.__class__):
            self.__d = deepcopy(d.__d)
        else:
            self.__d = deepcopy(d)

    def __getitem__(self, key):
        return self.__d[key]

    def __setitem__(self, key, value):
        self.__d[key] = value

    def __delitem__(self, key):
        del self.__d[key]

    def __iter__(self):
        return iter(self.__d)

    def __len__(self):
        return len(self.__d)

    def find(self, path, default=None):
        """
         Retrieves a single value using JSON-Pointer syntax
        """
        result = resolve_pointer(self.__d, path, default)
        if isinstance(result, dict):
            result = TDict(result)
        return result

    def setin(self, path, value):
        """
         Set a value using JSON-pointer syntax
        """
        set_pointer(self, path, value)
