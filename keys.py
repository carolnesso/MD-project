"""
GERADOR DE CHAVES (keys.py)
"""

import mdc

def calc_phi(p, q):
    return (p - 1)*(q - 1)

def calc_n(p, q):
    return p*q

def calc_d(e, phi):
    quocientes = mdc.quocientes_euclides(e, phi)
    quocientes.pop()
    quocientes.reverse()
    table = mdc.table_method(quocientes)
    
    if len(quocientes) % 2 == 0:
        table[-2] *= -1
    else:
        table[-1] *= -1
    
    while table[-2] < 0:
        table[-2] += phi

    return table[-2]