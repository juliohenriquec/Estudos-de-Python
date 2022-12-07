import random
chute = int(input('Pensei em um número de 1 a 5, qual número eu pensei? '))
lista = [1, 2, 3, 4, 5]
num = random.choice(lista)
print(f'Eu pensei no número {num}')
if chute == num:
    print('Parabens, você acertou!')
else:
    print('Voce errou!')
