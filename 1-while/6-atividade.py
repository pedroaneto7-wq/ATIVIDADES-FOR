import os
import time
os.system('cls')

quantedade = 3

while True:
    login = input('digite seu login')
    senha = input('digite sua senha')
    if login == 'pda' and senha == 'pn123':
        print('verificando login e senha...')

        print()
        print(f'Bem vindo de volta {login}')
        break
    else:
        print('login ou senha imcorreto')
    for i in range(quantedade):
        print('tente novamente')
    os.system('cls')
    break



