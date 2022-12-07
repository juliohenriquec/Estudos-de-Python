dis = float(input('Qual a distância em km de sua viagem? '))
if dis <= 200:
    preco = dis * 0.5
    print(f'O preço da sua passagem é R${preco}')
else:
    preco1 = dis * 0.45
    print(f'O preço da sua passagem é R${preco1}')
print('Tenha uma ótima viagem!')