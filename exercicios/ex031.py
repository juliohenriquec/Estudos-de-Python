dis = float(input('Qual a distância em km da sua viagem? '))
print(f'Você esta prestes a começar uma viagem de {dis}Km.')
if dis <= 200:
    preco = dis * 0.5
else:
    preco = dis * 0.45
print(f'O preço da sua passagem será de R${preco}')
print('Tenha uma ótima viagem!')
