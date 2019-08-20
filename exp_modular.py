"""
Realiza o cálculo da exponenciacao modular rapida

"""

def fast_mod_expn(num, exp, b):
	resultado = 1

	while True:
		if exp == 0:
			return resultado
		elif exp % 2 != 0:
			resultado = (num * resultado) % b
			exp = (exp - 1) // 2
		else:
			exp = exp // 2
		num = (num * num) % b

	return resultado

