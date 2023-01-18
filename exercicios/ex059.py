from time import sleep
opcoes = 0
print('=-=' * 10)
num1 = int(input('Digite um valor:'))
num2 = int(input('Digite outro valor:'))
print('=-=' * 10)
while opcoes != 5:
    print('''----O que voce deseja fazer?----
    [ 1 ] Somar os números
    [ 2 ] Multiplicar os números
    [ 3 ] Ver qual o maior número
    [ 4 ] Adicionar novos números
    [ 5 ] Sair do programa''')
    opcoes = int(input('>>>>Opção: '))
    if opcoes == 1:
        soma = num1 + num2
        print(f' {num1} + {num2} = {soma}')
    elif opcoes == 2:
        produto = num1 * num2
        print(f'{num1} x {num2} = {produto}')
    elif opcoes == 3:
        if num1 > num2:
            print(f'{num1} é o maior número.')
        else:
            print(f'{num2} é o maior número.')
    elif opcoes == 4:
        print('Informe os números novamente.')
        num1 = int(input('Digite um valor:'))
        num2 = int(input('Digite outro valor:'))
    elif opcoes == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Acabou!')
