import os
os.system('cls')
print('inserindo numeros no vetor=')
vetor_numero  = []

for i in range (3):
    numero = int(input('digite um numero'))
    vetor_numero.append(numero)


print('\n= exibindo numeros do vetor =')
for i in range(3):
    print(f'primeira posição do vetor:{vetor_numero[i]}')


