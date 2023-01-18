from random import randint
computador = randint(0, 10)
print('=' * 20)
print('Vou pensar num número entre 0 e 10. Tente adinvinhar... ')
print('=' * 20)
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Em que número eu pensei: '))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        elif jogador > computador:
            print('Menos... Tente novamente!')
print(f'Você acertou! E precisou de {cont} tentativa(s)')
print('----FIM----')

