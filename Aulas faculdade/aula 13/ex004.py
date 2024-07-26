
cont = 0
soma = 0
for c in range(0,6):
    num = int(input('Digite um número: '))
    if num % 2 ==1:
        soma += num
        cont += 1

print(f'A soma dos numeros ÍMPARES informados é de {soma}')