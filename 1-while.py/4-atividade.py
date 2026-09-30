import os
os.system('cls')

soma = 0
quantedade_notas = 2

for i in range (quantedade_notas):
    while True:
        nota = float(input(F'digite sua {i + 1} nota'))
        if nota < 0 or nota > 10:
            print('repetir nota')
        else:
            soma = soma + nota
            break

media = soma / quantedade_notas
print(f'media:{media}')
print('==FIM==')

