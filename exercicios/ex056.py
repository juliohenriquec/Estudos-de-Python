somaidade = 0
mediaidade = 0
nomemaisvelho = ''
maioridadehomem = 0
totmulher20 = 0
for p in range(1,5):
    print(f'----- {p}ª pessoa -----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo (M/F): ')).strip().upper()
    somaidade += idade
    if  p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome

    #número de mulheres com menos de 20
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('-----DADOS-----')
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho do grupo é o {nomemaisvelho} e tem {maioridadehomem} anos')
print(f'O número de mulher com menos de 20 anos no grupo é {totmulher20}')
