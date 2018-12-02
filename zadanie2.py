def odsetki(oproc, czas, kwota):
    twojeOdsetki = kwota * (oproc / 100) * (czas / 12)
    return twojeOdsetki

def odnawianie(oproc, czas, kwota, ileodnowien)
    kwota_bazowa = kwota
    for ile in range(ileodnowien):
            twojeOdsetki = odsetki(oproc, czas, kwota)
            kwota = kwota + twojeOdsetki
    return(kwota - kwota_bazowa)

odsetki(3,12,1000,0)
odsetki(3,3,1000,4)
