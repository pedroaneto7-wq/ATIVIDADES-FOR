import os
os.system('cls')
import time
soma = 0
quantedade_numero = 0


while True:
    os.system('cls')
    numero = int(input('digite um numero'))

    if numero >= 0:
        soma += numero
        quantedade_numero = 1
        time.sleep(2)
    else:
        break

    if quantedade_numero == 0:
        print('não foi iunserrido nenhum numero')
    else:
        emdia = soma / quantedade_numero
        print('media:')