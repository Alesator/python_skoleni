# coding: utf-8
'''
Ex Dict & Files: 3
Načti data ze soubory 'Engl_story.txt' a vypiš slovíčka,
která se v příběhu vyskytují více jak 3x.
Očekávaný výsledek:
8x : 'dad'
5x : 'is', 'son', 'the', 'bill', 'gates'
4x : 'to', 'of', 'my'
'''

fr = open('../resources/Engl_story.txt', 'r', encoding='utf-8')
str = (fr.read().replace('\n',' ')
       .replace(':',' ')
       .replace('.','')
       .replace('!','')
       .replace("'",''))

di = dict()
for x in str.lower().split(sep=' '):
    if len(x) > 0:
        if x in di:
            di[x] = di[x] + 1
        else:
            di[x] = 1

diRes = dict()
for k, v in di.items():
    if v > 3:
       if v in diRes:
          diRes[v].append(k)
          i = 1
       else:
          diRes[v] = []
          diRes[v].append(k)

print('\n'.join([f'{x}: {diRes[x]}' for x in sorted(diRes, reverse=True)]))

