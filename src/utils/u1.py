# coding: utf-8

from collections.abc import Iterable
from collections.abc import Callable
from typing import List

cnt: int = 0


def itr_filter(it: Iterable) -> List[int]:
    global cnt
    cnt += 1
    print(f'Pocet spusteni: {cnt}')
    return [x for x in it if type(x) == int]


def itr_bigger(it1: Iterable, it2: Iterable, filtr: Callable = itr_filter) -> Iterable:
    return it1 if filtr(it1) > filtr(it2) else it2


'''print(itr_filter( [1, 'x', 2, 'y', 3, 'z'] ))             # -> [1, 2, 3]
print(itr_filter( (1, 'a', 2, 'b', 'c', 4 ) ))            # -> [1, 2, 4]
print(itr_filter( {1:'v1', 'a':'v2', 5:'v3', 'b':'v4'} )) # -> [1, 5]

print (itr_bigger( [1, 'x', 2, 'y', 3, 'z'], (1, 'a', 2, 'b', 'c', 4 ) ))
print (itr_bigger( [1, 'x', 2, 'y', 3, 'z'], {1:'v1', 'a':'v2', 5:'v3', 'b':'v4'} ))'''