import os
os.system('cls')
import time
login_salvo= input('digite seu login:')
senha_salva = input('digite sua senha:')
os.system('cls')


while True:
    login = input('digite seu login')
    senha = input(' digite sua senha')
    if login == login_salvo and senha == senha_salva:
        print()
        print(f'Bem vindo de volta {login_salvo}')
        break
    else:
        print('verificando.....')
        time.sleep(1.3)
        print()
        print('login ou senha incorretos\n tente novamente! ')
        time.sleep(2)
        os.system('cls')


