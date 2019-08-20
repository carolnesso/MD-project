"""
CHECA SE UM NUMERO DADO É PRIMO (prime.py)
"""
from math import sqrt
 
def is_prime(n):
    i = 2
    cont = 0
    while i < sqrt(n):
        if n % i == 0:
            cont += 1
        i += 1
    if cont < 2:
        return True
    else:
        return False