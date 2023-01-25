while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print('=' * 13)
    for c in range(0, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('=' * 13)
print('Fim do programa')
