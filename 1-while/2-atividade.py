import os
os.system('cls')

while True:
    nota = int(input('digite sua nota:'))
    if nota <0 or nota >10:
        print('digite novamente:')
    else:
        print('sua nota esta dentro da media')
        break
print('==fim==')

