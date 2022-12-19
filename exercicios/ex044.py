valor = float(input('Qual o valor do produto? R$'))
print('Qual a forma de pagamento?\n'
      '[1] - À vista, dinheiro ou cheque.\n'
      '[2] - À vista no cartão de débito .\n'
      '[3] - Em até 2x no cartão de crédito.\n'
      '[4] - 3x ou mais no cartão')
pagamento = int(input('Opção: '))
if pagamento == 1:
    valor = valor - valor*0.10
    print(f'Preço com 10% de desconto: R${valor}')
elif pagamento == 2:
    valor = valor - valor*0.05
elif pagamento == 3:
    int(input('número de parcelas: '))
    print(f'Preço formal: R${valor}')
elif pagamento == 4:
    int(input('número de parcelas: '))
    valor = valor + valor*0.20
    print((f'Preço com 20% de juros: R${valor}'))
    