from random import choice
print('\033[1;34m='*30)
print('Jogo do Pedra, Papel, Tesoura')
print('='*30)

lista = ['PEDRA', 'PAPEL', 'TESOURA']
player = str(input('\033[mSua jogada: ')).upper()
IA = choice(lista)
print(f'Jogada adversária: \033[31m{IA}\033[m')

#Jogador vence se:
if player == 'PEDRA' and IA == 'TESOURA':
    print('\033[35mPEDRA ganha de TESOURA!')
    print('\033[1;32mVocê venceu!')
elif player == 'PAPEL' and IA == 'PEDRA':
    print('\033[35mPAPEL ganha de PEDRA!')
    print('\033[1;32mVocê venceu!')
elif player == 'TESOURA' and IA == 'PAPEL':
    print('\033[35mTESOURA ganha de PAPEL')
    print('\033[1;32mVocê venceu!')
#IA vence se:
elif IA == 'PEDRA' and player == 'TESOURA':
    print('\033[35mPEDRA ganha de TESOURA!')
    print('\033[1;31mVocê perdeu!')
elif IA == 'PAPEL' and player == 'PEDRA':
    print('\033[35mPAPEL ganha de PEDRA!')
    print('\033[1;31mVocê perdeu!')
elif IA == 'TESOURA' and player == 'PAPEL':
    print('\033[35mTESOURA ganha de PAPEL')
    print('\033[1;31mVocê perdeu!')
else:
    print('\033[1;33mEMPATE!\033[m')