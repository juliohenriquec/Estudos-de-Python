from random import randint #importando randint

#sorteando os numeros na tupla numeros
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)

#mostrando os valores soretados
print("Os valores sorteados foram : ", end = '')
for n in numeros:
    print(f'{n} ', end = '')

#mostrando o maior valor
print(f"\nO maior valor sorteado foi {max(numeros)}")
#mostrando o menor valor
print(f"O menor valor sorteado foi {min(numeros)}")
