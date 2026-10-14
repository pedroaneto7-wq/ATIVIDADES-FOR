import os
os.system('cls')

vetor_livros = []

for i in range(5):
    livros = input('digi o nome do seu livro:')
    vetor_livros.append(livros)
    
for i in vetor_livros:
    print(f'livors: {i}')