nome = str(input('Qual seu nome completo? ')).strip()

print('Analisando seu nome...')

print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

tamanho = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {tamanho} letras')


lista = nome.split()
nome1 = len(lista[0])
print(f'Seu primeiro nome é {lista[0].title()} e ele tem {nome1} letras')


