n = int(input('Digite um número:'))
print('\033[31m=' * 13)
for c in range(0, 11):
    print(f'\033[32m{n} x {c:2} = {n * c}')
print('\033[31m=' * 13)

