continua = 'S'
cont = soma = maior = menor = 0
while continua in 'S':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = str(input('Deseja continuar?[S/N]: ')).upper()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}.\nO maior valor foi {maior} e o menor foi {menor}.')
