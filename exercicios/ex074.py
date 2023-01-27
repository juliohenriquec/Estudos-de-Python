from random import randint
cont = maior = menor = 0
print('Gerador de números aleatórios')
print('------------------------------')
print('Números gerados:' )
for c in range(0, 5):
    numeros = randint(1, 10)
    cont +=1
    listagem = (numeros)
    print(listagem, end=' ')
    if cont == 1:
       menor = maior = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
print('\n------------------------------')
print(f'O maior número gerado foi {maior}')
print(f'O menor número gerado foi {menor}')
