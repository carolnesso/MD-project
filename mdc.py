"""
MDC e TESTE COPRIMOS/ (mdc.py)
"""
def mdc_euclides(a, b):
    rest = a % b
    
    if rest == 0:
        return b
    else:
        return mdc_euclides(b, rest)

def quocientes_euclides(n1, n2):

    rest = int(n1 % n2)
    lista = []
    
    while rest != 0:
        lista.append(int(n1 / n2))
        n1 = n2
        n2 = rest
        rest = n1 % n2
    lista.append(int(n1/n2))

    return lista

def table_method(lista):
    n_lista = [1]
    n_lista.append(n_lista[0] * lista[0])
    
    for i in range(1, len(lista)):
        n_lista.append(n_lista[i] * lista[i] + n_lista[i-1])
    
    return n_lista 