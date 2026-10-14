import os
os.system('cls')

media = 0

for i in range(3):
    nota=float(input('digite a nota:'))

    media += nota / 3

print(media)

if media >=7:
        print('aprovado')
elif media >=5:
        print('recuperação')
else:
        print('reprovado')

