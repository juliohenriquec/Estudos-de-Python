tupla = ('APRENDER', 'PROGRAMAR', 'LIGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR')
vogal = ('a', 'e', 'i', 'o', 'u')
for p in tupla:
    print(f'Vogais da palavra {p}:', end=' ')
    for letra in p:
        if letra.lower() in vogal:
            print(f'{letra.lower()}', end=' ')
    print()

