num = int(input('Fatorial de: '))
cont = num
f = 1
print(f'Calculando {num}!')
while cont > 0:
    print(f'{cont}', end=' ')
    print('x' if cont > 1 else '=', end=' ')
    f *= cont
    cont -= 1
print(f'{f}')


