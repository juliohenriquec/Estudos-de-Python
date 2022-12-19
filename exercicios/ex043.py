peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / altura ** 2
print(f'Seu IMC é igual a {IMC:.2f}')
if IMC < 18.5:
    print('Você está Abaixo do Peso.')
elif 18.5 <= IMC <= 25:
    print('Você tem o Peso Ideal.')
elif 25 < IMC <= 30:
    print('Você está com Sobrepeso.')
elif 30 < IMC <=40:
    print('Você está Obeso.')
elif 40 < IMC:
    print('VocÊ está com Obesidade Mórbida.')
