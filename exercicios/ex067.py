while True:
    n = int(input('\033[mDigite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('\033[31m=' * 13)
    for c in range(0, 11):
        print(f'\033[32m{n} x {c:2} = {n * c}')
    print('\033[31m=' * 13)
print('Fim do programa')