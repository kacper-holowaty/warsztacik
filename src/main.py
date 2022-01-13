

def funkcja(liczba1,liczba2):
    if liczba1 > liczba2:
        return liczba1
    elif liczba1 < liczba2:
        return liczba2
    elif liczba1 == liczba2:
        return liczba1

print(funkcja(funkcja(20,34),7))
