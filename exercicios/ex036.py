valor = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você deseja financiar a casa? '))
prestação = valor /(anos * 12)
mínimo = salário * 0.3
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos, a prestação será de R${prestação:.2f}.')
if prestação <= mínimo:
    print('\033[32mEmpréstimo CONCEDIDO!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')
