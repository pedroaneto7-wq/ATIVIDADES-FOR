import os
os.system('cls')
print('inserindo numeros no vetor=')
vetor_numero  = []

for i in range (3):
    numero = int(input('digite um numero'))
    vetor_numero.append(numero)


print('\n= exibindo numeros do vetor =')
for valor in vetor_numero:
    print(f'valor:{valor}')
