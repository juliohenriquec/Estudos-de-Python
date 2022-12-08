vel = int(input('Qual a velocidade atual do veículo? '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'MULTADO! Você excedeu o limite de velocidade que é 80Km/h. Você deve pagar uma multa de R${multa: 0.2f}')
print('Bom dia! Dirija com segurança')
