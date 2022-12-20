from datetime import date
nasc = int(input('Ano de Nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    print(f'O atleta tem {idade} anos e faz parte da categoria MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e faz parte da categoria INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e faz parte da categoria JÚNIOR.')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e faz parte da categoria SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos e faz parte da categoria MASTER.')