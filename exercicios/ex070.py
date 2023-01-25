print('=====MERCADO FREE=====')
total = tot1000 = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: ')).strip().upper()
    valor = float(input('Preço do Produto:R$'))
    cont += 1
    total += valor
    if valor > 1000:
        tot1000 += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar comprando?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total da compra foi de R${total:.2f}')
print(f'{tot1000} produtos comprados custaram mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custou R${menor}')

