import os
os.system ('cls')


while True:
    numero= int(input('digite um numero:'))
    if numero <1 or numero >10:
        print('numero invalido, tentar novamente!')
    else:
        print('o numero esta entre 1 e 10.')
        break

print('= fim=')
