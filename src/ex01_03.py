# coding: utf-8

'''
Ex List: 3
Ze vstupního listu vytvoř list nový, ale bez prázdných řetězců.
Očekávaný výsledek:
[ 'alfa', 'gama', ' ']
'''

ls = [ 'alfa', '', 'gama', '', ' ']
ls2 = [x for x in ls if len(x) > 0]
print(ls2)
