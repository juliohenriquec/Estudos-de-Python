from random import randint
cont = 0
print('---Jogo do Par ou Ímpar!---')
while True:
    num = int(input('Digite um número:'))
    IA = randint(1, 10)
    escolha = str(input('Voce quer par ou ímpar?[P/I] ')).strip().upper()[0]
    soma = IA + num
    print(f'Você jogou {num} e o computador {IA}. O total foi {soma}.')
    print('DEU PAR!')
    if soma % 2 == 0:
        if escolha == 'P':
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    elif soma % 2 != 0:
        if escolha == 'I':
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'FIM DE JOGO')
print(f'Você venceu por {cont} vezes consecutivas!')

