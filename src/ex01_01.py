# coding: utf-8

'''
Ex List: 1
Najdi a vytiskni DRUHÉ nejvyšší číslo z listu ls
Očekávaný výsledek:
42
'''

ls = [10, 21, 42, 18, 99, 32, 11]
print(sorted(ls, reverse = True)[1])