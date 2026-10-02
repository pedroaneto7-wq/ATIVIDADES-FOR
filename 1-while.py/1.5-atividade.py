import os
os.system('cls')

nota = float(input(' digite uma nota entre 0 e 10:'))

while True:
    if nota < 0 or nota >10:
        print('vc perdeu')
        print()
        print('tente novamente')
    else:
        print('não fez mais que a obrigação')
    break
