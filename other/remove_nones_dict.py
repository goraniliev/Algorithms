# -*- coding: utf-8 -*-

__author__ = 'goran'


def remove_none(obj):
    if isinstance(obj, (list, tuple, set)):
        return type(obj)(remove_none(x) for x in obj if x is not None)
    elif isinstance(obj, dict):
        return type(obj)((remove_none(k), remove_none(v))
                         for k, v in obj.items() if k is not None and v)
    else:
        return obj

d = {'a': 'AAA', 'b': {'b': 'BBB', 'c': None}, 'd': None, 'e': ''}
print(remove_none(d))
