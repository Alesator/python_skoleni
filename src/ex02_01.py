# coding: utf-8

'''
Ex Dict & Files: 1
Načti data ze souboru 'TopTen.txt':
-- Artist -- | -- Single -- | -- Weeks --
Ezra George | Green Green Grass | 14
Styles Harry | As It Was | 37
Capaldi Lewis | Forget Me | 12
^^-- EOF --^^
a vytvoř nový soubor 'TopTen_sorted.txt' s údaji
setříděné podle počtu týdnů v TopTen od nejvyššího čisla po nejnižsí ve formátu:
-- Weeks -- | -- Single -- | -- Artist --
Očekávaný výsledek 'TopTen_sorted.txt':
-- Weeks -- | -- Single -- | -- Artist --
37 | As It Was | Styles Harry
14 | Green Green Grass | Ezra George
12 | Forget Me | Capaldi Lewis
^^-- EOF --^^
'''

fr = open('../resources/TopTen.txt', 'r', encoding='utf-8')
resArr = []
resTitle = []

for line in fr:
    arr = line.split(sep='|')
    if line.find('-- Weeks --') == -1:
        resArr.append(arr)
    else:
        resTitle = arr

resArr = sorted(resArr, key=lambda i: i[2], reverse=True)
resArr.insert(0, resTitle)

fw = open('../resources/TopTen_sorted.txt', 'w', encoding='utf-8')
fw.writelines(f'{x[2].rstrip()}|{x[1].rstrip()}|{x[0].rstrip()}\n' for x in resArr)


