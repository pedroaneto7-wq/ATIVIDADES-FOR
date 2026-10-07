import os
os.system('cls')


soma = 0
contador = 0


while True:
    nota =float(input('digite sua nota'))
    resposta = input(' deseja adicionar mais nota (s/n):').upper()
    if resposta == "S":
        soma += nota
        contador += 1
        print()
        print(f'contador {contador}')
    elif resposta == "N":
        soma  += nota
        contador += 1
        media = soma / contador
        print(f'media: {media}')
        break
    else:
        input('esse caracter não funciona nessa sequencia,precione qualquer butão')
        os.system('cls')
