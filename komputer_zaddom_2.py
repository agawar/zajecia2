import random

def strategia(stan_gry):
    ruch = min(stan_gry, random.randint(1, 3))
    return ruch

def strategia2(stan_gry):
    ruch = min(3, stan_gry)
    return ruch