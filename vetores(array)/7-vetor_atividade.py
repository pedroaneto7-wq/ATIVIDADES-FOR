import os
os.system('cls')

vetor_numero = []
QUANTEDADE_NUMEROS = 5
soma = 0
negativo = 0

for i in range (QUANTEDADE_NUMEROS):
    numero = int(input('digite um numerto'))
    vetor_numero.append(numero)
if numero > 0:
    soma += numero
elif numero < 0:
    negativo += 1

print(f'soma positivos: {soma}')
print(f'quantedade de numeros negativos: {negativo}')
