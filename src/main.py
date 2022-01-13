lista = [2, 4, 7, 8, 10, 16, 24, 29, 31]
lista2 = lista[1:len(lista)]

def czy_posortowana(lista):
    for i in lista:
        for j in lista2:
            if i > j:
                return False
        return True
print(czy_posortowana(lista))

