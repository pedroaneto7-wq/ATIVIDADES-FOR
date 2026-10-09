import os
os.system('cls')

vetor_nome = []

for i in range(4):
    nome = int(input('digite seu nome'))
    vetor_nome.append(nome)

for i in range(4):
    print(f'nome {vetor_nome}')