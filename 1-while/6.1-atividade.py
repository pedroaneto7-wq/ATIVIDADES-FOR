import os
os.system('cls')
import time
soma = 0
QUANTEDADE_NOTAS = 2

for i in range(QUANTEDADE_NOTAS):
    while True:
        nota = int(input('digite sua nota'))
        if nota < 0 or nota > 10:
            time.sleep(1)
            print('vc errou tente novamente')
        else:
            soma = soma + nota
            break
media  = soma / QUANTEDADE_NOTAS
print(f'media{media}')
print('VLW')

