print('Parabens, voce ganhou um aumento!')
salario = float(input('Informe seu salário atual: R$ '))
if salario > 1250:
    aumento = (salario * 0.1) + salario
    print(f'Seu salário recebeu um aumento de 10%, a partir de agora você passará a rebecer R${aumento: .2f} por mês.')
else:
    aumento = (salario * 0.15) + salario
    print(f'Seu salário recebeu um aumento de 15%, a partir de agora você passará a rebecer R${aumento: .2f} por mês.')
