sexo = str(input('Digite seu gênero[M/F/N]: ')).upper().strip()[0]
while not sexo in 'MFN':
        sexo = str(input('Dados inválidos, por favor informe seu gênero: '))
print(f'Gênero {sexo} registrado com sucesso.')


