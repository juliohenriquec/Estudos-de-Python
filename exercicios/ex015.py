dias = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos Km foram percorridos com o carro? '))
preço = (dias * 60) + (km * 0.15)
print(f'Você pagará pelo o aluguel desse carro R${preço: .2f}')
