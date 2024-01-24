#criando a tupla e pedindo os valores
numeros = (int(input("digite um número: ")), int(input("digite outro número: ")), int(input("digite mais um número: ")),
           int(input("digite o último número: ")))

#mostrando os valores
print(f'Você digitou os valores {numeros}')

#quantas vezes o valor 9 apareceu
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')

#quando o número 3 apareceu pela primeira vez
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

#qual dos números sorteados são pares
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end = " ")
print('')