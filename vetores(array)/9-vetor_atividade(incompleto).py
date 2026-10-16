import os
os.system('cls')
vetor_comida = []
picanha = 25
lasanha = 20
strongonoff = 18
bifi_acebolado = 15
pão_com_ovo = 5

while True:
    os.system("cls")
    print('''
1- Picanha        R$ 25,00
2- lasanha        R$ 20,00
3- strongonoff    R$ 18,00
4- bifi acebolado R$ 15,00
5- pão com ovo    R$ 5,00 ''')
    menu = int(input('fale seu pedido:'))
    match menu:
        case '1':
            print(f'picanha, valçor: {picanha}')
            vetor_comida.append(25)
            repitir = input('deseja outro pedido? ').upper()
            if repitir == 'N':
                break
        case '2':
            print(f'lasanha, valor: {lasanha} ')
            vetor_comida.append(20)
            repitir = input('deseja outro pedido? ').upper()
            if repitir == 'N':
                break
        case '3':
            print(f'strongonoff, valor: {strongonoff}')
            vetor_comida.append(18)
            repitir = input('deseja outro pedido? ').upper()
            if repitir == "N":
                break
        case '4':
            print(f'bifi_acebolado, valor: {bifi_acebolado}')
            vetor_comida.append(15)
            if repitir == 'N':
                break
        case '5':
            print(f'pão com ovo, valor: {pão_com_ovo}')
            vetor_comida.append(5)
            if repitir == 'N':
                break
        case ___:
            print()
            
soma = sum(vetor_comida)
print(f'valor, {soma}')


    
