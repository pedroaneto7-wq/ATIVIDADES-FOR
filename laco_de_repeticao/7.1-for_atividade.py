import os
os.system('cls')

pares = 0
impares = 0


for i in range(2):
    numero = int(input(f'digite {i+1}° numero: '))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1


print(f'pares {pares}')
print(f'impares {impares}')