# coding: utf-8

'''
Ex 1.4
Na základě vstupního listu vytiskni formátovanou tabulku, kde:
* na jméno je vyhrazeno 10 pozic a je zarovnané doleva a
* na číslo je vyhrazeno 5 pozic a je zarovnané doprava
Očekávaný výsledek:
'Pepa : 30'
'Eva : 280'
'Jarda : 3'
'''

# maxLenName = len((sorted(s, key=lambda i: len(i[0]), reverse=True)[0])[0]) + 2
# maxLenNum = len(str((sorted(s, key=lambda i: len(str(i[1])), reverse=True)[0])[1])) + 2

s = [['Pepa', 30], ['Eva', 280], ['Jarda', 3]]
print('\n'.join([f"'{x[0]:<10}:{x[1]:>5}'" for x in s]))
