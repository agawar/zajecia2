import math

def jakzaplacic(kwota):
    nominaly = [20, 10, 5, 2, 1]
    liczbamonetlubbanknotow = []

    for nominal in nominaly:
        suma = ilemonetlubbanotow(kwota, nominal)
        liczbamonetlubbanknotow.append(suma)
        kwota = kwota - suma*nominal
        print("{1} bankotow/monet {0} zł".format(nominal, suma))

    print(liczbamonetlubbanknotow)

def ilemonetlubbanotow(pieniadze, nominal):
    return math.trunc(pieniadze/nominal)

jakzaplacic(123)
jakzaplacic(98)


def rozmien(portfel, kwota):

    portfel_owdr = portfel[::-1]
    print(portfel_owdr)

    liczbamonetlubbanknotow = []
    kwotaDoWydania = kwota

    for i in range(len(portfel)):
        if portfel[-i] != 0 and portfel[i]*i >= kwotaDoWydania:
            ilemonetlubbanknotow = kwotaDoWydania//portfel[i]


