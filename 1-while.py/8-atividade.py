import os
os.system('cls')

QUANTEDADE_NOTA = 3
soma = 0
while True:
    for i in range(QUANTEDADE_NOTA):
        nota = input('digite sua nota')
        if nota < 0 or nota > 10:
            print('reprovado\n tente novament')
            print()
        
        else:
            soma = soma + nota
            break
        media = soma / QUANTEDADE_NOTA
        print(f'media{media}')
        