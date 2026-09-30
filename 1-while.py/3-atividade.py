import os
os.system('cls')


soma = 0

quantedade_notas = 2

for i in range (quantedade_notas):
    while True:
        nota = float(input(f'digite sua {i +1} nota:'))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break
        else:
            print()
            print('favor repetir sua nota')

media = soma / quantedade_notas

print(f'media:{media}')
print('==FIM==')