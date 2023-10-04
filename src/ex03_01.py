# coding: utf-8

import sys

s = 'alfa'
ls = [1, 2]
dc = {'a':'aa', 'b':'bb'}


def log(arg1, arg2, arg3, sep = '|', end = '$$\n'):
    sys.stdout.write(sep.join([str(x) for x in [arg1, arg2, arg3]]) + end)


log( s, ls, dc )                         # -> alfa-|-[1, 2]-|-{'a': 'aa', 'b': 'bb'}$$
log( s, ls, dc, sep='<->' )              # -> alfa<->[1, 2]<->{'a': 'aa', 'b': 'bb'}$$
log( s, ls, dc, sep='<->', end='oo' )    # -> alfa<->[1, 2]<->{'a': 'aa', 'b': 'bb'}oo

