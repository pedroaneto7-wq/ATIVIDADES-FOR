import os
os.system('cls')

soma = 0
quantedade_nota = 0

while True:
    print('''
==== MENU ====
S - inserir uma nota
N - calcular media
''')

    resposta = input('deseja inserir uma nota?'). lower()

    match resposta:
        case "s":
            nota = float(input('digite uma nota: '))
            soma += nota
            quantedade_nota += 1 
        case "n":
            if quantedade_nota == 0:
                print('não foram inseridas notas \n')
                break
            else :
                break
        case _:
            print('opição invalida \n')
            input('aperte qualquer butão para conntinuar')
media = soma / quantedade_nota
print(f'media: {media}')
