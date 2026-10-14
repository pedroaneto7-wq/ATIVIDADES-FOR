import os
os.system('cls')
print('inserindo numeros no vetor=')
vetor_numero  = []


numero = int(input('digite um numero'))
vetor_numero.append(numero)
numero = int(input('digite um numero'))
vetor_numero.append(numero)
numero = int(input('digite um numero'))
vetor_numero.append(numero)

print('\n= exibindo numeros do vetor =')
print(f'primeira posição do vetor:{vetor_numero[0]}')
print(f'ultima posição do vetor: {vetor_numero[2]}')


