# coding: utf-8

import sys

a, b, s, ls, dc = 1, 2, 'alfa', [1, 2], {'a':'aa', 'b':'bb'}


def log(*args, sep = '|', end = '$$\n'):
    sys.stdout.write(sep.join([str(x) for x in args]) + end)


log( a, b, s, ls, dc, sep='<->', end='oo' )
