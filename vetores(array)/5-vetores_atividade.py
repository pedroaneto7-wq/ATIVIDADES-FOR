import os
os.system('cls')

vetor_nota = []

for i in range(3):
    nota = float(input('digite sua nota'))
    vetor_nota.append(nota)
    
    for i in vetor_nota:
        print(f'nota: {vetor_nota}')