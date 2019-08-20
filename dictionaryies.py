"""
DICIONARIOS (dictionaryies.py)
"""      

"""
De acordo com a chamada da função, pode:
1. gerar um dicionário onde as chaves são as letras e os valores são os numeros equivalentes
2. gerar um dicionário onde as chaves são os numeros e os valores são as letras equivalentes

"""
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
letter_numbers = {}
def code_letters():
    j = 0
    for i in letters:
        letter_numbers[i] = j
        j+=1
    return letter_numbers

numbers_letters = {}
def letters_code():
    j = 0
    for i in letters:
        numbers_letters[j] = i
        j+=1
    return numbers_letters
