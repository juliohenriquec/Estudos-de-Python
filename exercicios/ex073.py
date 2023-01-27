equipes = ('RedBull', 'Ferrari', 'Mercedes', 'Alpine', 'McLaren', 'AlfaRomeo', 'Aston Martin', 'Hass', 'AlphaTauri', 'Willians')
print('-=' * 15)
print(f'As equipes que formam o grid da Formula 1 em ordem alfabética são: {sorted(equipes)}')
print('-=' * 15)
print(f'As cinco primeiras equipes do campeonato de 2022 são {equipes[0:5]}')
print('-=' * 15)
print(f'As quatro ultimas equipes do campeonato de 2022 são{equipes[-4:]}')
print('-=' * 15)
print('E a AlfaRomeo está na {}ª posição'.format(equipes.index('AlfaRomeo')+1))
print('-=' * 15)




