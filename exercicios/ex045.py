from random import randint
from time import sleep

print('\033[1;34m='*30)
print('Jogo do Pedra, Papel, Tesoura')
print('='*30)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
IA = randint(0,2)

print('''\033[mSua opções:
 [0] PEDRA
 [1] PAPEL
 [2] TESOURA''')
player =int(input('Sua jogada: '))

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!!!')
sleep(1)

print('-='*12)
print(f'Computador jogou {itens[IA]}')
print(f'Jogador jogou {itens[player]}')
print('-='*12)

if IA == 0: #computador joga pedra
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('COMPUTADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA! Tente novamente.')
elif IA == 1: #computador joga papel
    if player == 0:
        print('COMPUTADOR VENCE')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA! Tente novamente.')
elif IA == 2: #computador joga tesoura
    if player == 0:
        print('JOGADOR VENCE')
    elif player == 1:
        print('COMPUTADOR VENCE')
    elif player == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA! Tente novamente.')