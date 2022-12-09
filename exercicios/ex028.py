from random import randint
from time import sleep
computador = randint(0, 5)
print('=' * 20)
print('Vou pensar num número entre 0 e 5. Tente adinvinhar... ')
print('=' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
print(f'Eu pensei no número {computador}')
if jogador == computador:
    print('Parabens, você acertou!')
else:
    print('Voce errou!')

