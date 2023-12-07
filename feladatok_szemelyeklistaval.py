"""Készítsz metódust amely kiszamolja a szemelyek atlag életkorát """

def atlageletkor(lista):
    osszeg:int=0
    for i  in range (0,len(lista),1):
        osszeg += lista[i].kor
    return osszeg/len(lista)



"""Készíts metódust, mely megmondja a listaban lévő nők számát"""

def nokszam(lista):
    mennyiseg:int=0
    for i in range(0,len(nokszam),1):
        nem = lista[i].nem
        if nem ==" nő":
            mennyiseg+=1
    return mennyiseg



