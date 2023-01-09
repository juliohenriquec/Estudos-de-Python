from datetime import date
cont = 0
print('Informe o ano de nascimento de 7 pessoas.')
for c in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    idade = date.today().year - nasc
    if idade < 21:
        cont += 1
print(f'Dessas 7 pessoas, {cont} pessoas ainda não atingiram a maioridade e as outras {c - cont} já atingiram.')
