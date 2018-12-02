def pierwsza1(liczba):
    for i in range(1, liczba):
        if liczba % i == 0 and i != 1 and i != liczba:
            return False
    return True

def pierwsza2(liczba):
    dzielniki = []

        for dzielnik in range(1, liczba):
            if liczba % dzielnik == 0:
                dzielniki.append(dzielnik)
    if dzielniki == [1]:
        return True
    return False


print(pierwsza1(2))
print(pierwsza1(4))
print(pierwsza1(5))