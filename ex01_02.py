# coding: utf-8

'''
Ex List: 2
V níže uvedeném listu ls jsou řádky, které jsme načetli z log souboru.
Vytiskni na obrazovku řádky obsahující 'ERR:' a to bez ohledu na velikost
písmen.
Očekávaný výsledek:
'err: chybný vstup'
'!! ERR: nesprávné přihlašovací údaje !!',
'''

ls = [ 'První řádek načtený ze souboru',
'err: chybný vstup',
'Třetí řádek',
'!! ERR: nesprávné přihlašovací údaje !!',
'Další řádky',
]

print ('\n'.join([x for x in ls if x.upper().find('ERR') >= 0]))

