from datetime import date
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - ano
if idade <= 9:
    print(f'O atleta tem {idade} anos e faz parte da categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'O atleta tem {idade} anos e faz parte da categoria INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'O atleta tem {idade} anos e faz parte da categoria JÚNIOR.')
elif idade > 19 and idade <= 25:
    print(f'O atleta tem {idade} anos e faz parte da categoria SÊNIOR.')
elif idade > 25:
    print(f'O atleta tem {idade} anos e faz parte da categoria MASTER.')