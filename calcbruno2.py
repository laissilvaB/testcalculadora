# interface da calculadora

from calcbruno import soma
from calcbruno import sub
from calcbruno import multi
from calcbruno import div

def exibir_menu():
    print('-> 1 = Soma')
    print('-> 2 = Subtraçao')
    print('-> 3 = Multiplicação')
    print('-> 4 = Divisão')
    print('-> 0 = Sair')

# apresentação
print('\n\t\t\t --- Calculadora 2 ---\n')

while True:

    exibir_menu()
    opcao = int(input('\n --> Escolha a função <-- '))

    if opcao == 1:
        num1 = int(input('informe o N1: '))
        num2 = int(input('informe o N2: '))

        total = soma(num1, num2)

        print(f'{num1} + {num2} = {total}')
        print('===========================================')

    elif opcao == 2:
        num1 = int(input('Informe o N1: '))
        num2 = int(input('Informe o N2: '))

        total = sub(num1, num2)

        print(f'{num1} - {num2} = {total}')
        print('===========================================')

    elif opcao == 3:
        num1 = int(input('Informe o N1: '))
        num2 = int(input('Informe o N2: '))

        total = multi(num1, num2)

        print(f'{num1} X {num2} = {total}')
        print('===========================================')

    elif opcao == 4:
        num1 = int(input('Informe o N1: '))
        num2 = int(input('Informe o N2: '))

        total = div(num1, num2)

        print(f'{num1} / {num2} = {total}')
        print('===========================================')

    elif opcao == 0:
        print('\n\t\t\t ===== Saindo... Até mais!! :) ====== ')
        break

    else:
        print('\n\t\t\t ***** Opção Invalida, tente novamente ******')
