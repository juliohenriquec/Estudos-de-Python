cidade = str(input('Digite o nome de uma cidade: ')).upper().strip()
lista = cidade.split()
check = 'SANTO' in lista[0]
print(f'{cidade.title()} começa com a palavra "Santo"?')
print(check)
