nome = str(input('Qual seu nome completo? ')).strip().upper()
lista = nome.split()
print(f'Seu primeiro nome é {lista[0].title()} e seu ultimo nome é {lista[len(lista)-1].title()}.')
