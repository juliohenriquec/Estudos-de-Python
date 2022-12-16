from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
falta = 18 - idade
passou = idade - 18
if idade == 18:
    print('Você tem 18 anos. É a hora exata para você realizar seu alistamento militar.')
elif idade < 18:
    print(f'Você tem {idade} anos. Ainda falta {falta} anos para você ter que realizar seu alistamento militar.')
else:
    print(f'Você tem {idade} anos. Se você não fez seu alistamento militar, corra para fazer pois você está {passou} anos atrasado.')

