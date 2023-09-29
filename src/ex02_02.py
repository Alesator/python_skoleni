# coding: utf-8
'''
Ex Dict & Files: 2
Načti data ze soubory 'Engl_story.txt'
a vytiskni počet různých slovíček v příběhu.
Očekávaný výsledek: 33
'''

fr = open('../resources/Engl_story.txt', 'r', encoding='utf-8')
str = (fr.read().replace('\n',' ')
       .replace(':',' ')
       .replace('.','')
       .replace('!','')
       .replace("'",''))

arr = str.upper().split(sep=' ')
setRes = set()

for x in arr:
    if len(x) > 0:
        setRes.add(x)

print(len(setRes))
