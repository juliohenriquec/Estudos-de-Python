vel = int(input('Qual a velocidade atual do veículo? '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado, sua multa é de R${multa: 0.2f}')
print('Bom dia! Dirija com segurança')
