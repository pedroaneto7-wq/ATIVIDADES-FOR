import os
os.system('cls')


while True:


    print('''
======= cardapio =====
1- PF
2-CARNE COM FRITAS
3-CAMARÃO
4-MACARÃO
5-PRATO DA CASA''')
    numero = input('digite seu pedido:')
    match numero:

        case '1':
            print('PF',20.00)
            break
        case '2':
            print('CARNE COM FRITAS',35.00)
            break
        case '3':
            print('CAMARÃO',100.00)
            break
        case '4':
            print('MACARONADA',45.00 )
            break
        case '5':
            print('PRATO DA CASA',50.00)
            break
        case __:
            print()














