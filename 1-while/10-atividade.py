import os
os.system('cls')

soma = 0
contador = 0

while True:
    valor = int(input('digite um valor:'))
    if valor < 0:
        break
    soma += valor
    contador += 1
    if contador >0:
        media = soma / contador
        print(f'a media é: {media}')
    else:
        print('nenhum valor positivo foi inserido.')
        
   