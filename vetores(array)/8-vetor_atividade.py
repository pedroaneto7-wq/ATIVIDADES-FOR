import os
os.system('cls')

vetor_numero = []
QUANTEDADE_NUMERO = 5

for i in range(QUANTEDADE_NUMERO):
    numero = int(input('digite um numero:'))
    if numero < 0:
        numero = 0
    vetor_numero.append(numero)

for i, numero in enumerate(vetor_numero, start=1):
    print(f'{i}°numero: {numero}')