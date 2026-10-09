import os
import time
os.system('cls')

while True:
    senha = input('digite sua senha:')
    login = input('digite seu login:')
    if senha =="pn123"  and login == "pda":
        print('verificando login e senha')
        time.sleep(1.1)
        print()
        print(f'Bem-vindo de volta!!! {login}')
        break
    else:
        print('verificando login e senha....')
        time.sleep(1.2)
        print('login oun senha invalidos')
        print('tente novament\n')
        time.sleep(1)
        os.system('cls')




