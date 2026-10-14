import os
os.system('cls')
vetor_nota = []
QUANTEDADE_NOTAS = (3)
for i in range(3):
    nota = float(input('digite sua nota:'))
    vetor_nota.append(nota)
    
media = sum(vetor_nota)/ QUANTEDADE_NOTAS

for i in vetor_nota:
    print(f'nota: {vetor_nota}')
    
print(f'media: {media}')