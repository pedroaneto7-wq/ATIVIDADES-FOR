import os
os.system('cls')

pares = 0
impares = 0

for i in range(5):
    numero = int(input('digite o numero: '))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f'quantedade de pares: {pares} ')
print(f'quantedade de impares:{impares} ')

print('FIM')