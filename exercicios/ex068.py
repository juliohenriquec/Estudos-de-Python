from random import randint
cont = 0
IA = randint(1, 10)
print('---Jogo do Par ou Ímpar!---')
while True:
    num = int(input('Digite um número:'))
    escolha = str(input('Voce quer par ou ímpar? ')).strip().upper()
    soma = IA + num
    print(f'Jogada do Adversário:{IA}')
    if escolha == 'PAR':
        computador = 'ÍMPAR'
    if escolha == 'ÍMPAR':
        computador = 'PAR'
    if soma % 2 == 0:
        print(f'O resultado é {soma}.Deu par!')
        if escolha == 'PAR':
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    if soma % 2 != 0:
        print(f'O resultado é {soma}.Deu ímpar!')
        if escolha == 'ÍMPAR':
            print('Você venceu!')
            cont+= 1
        else:
            print('Você perdeu!')
            break
print(f'FIM DE JOGO')
if cont > 0:
    print(f'Você venceu por {cont} vezes consecutivas!')



