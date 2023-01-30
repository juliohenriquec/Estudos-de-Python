listagem = (int(input('Digite um valor: ')),
int(input('Digite outro: ')),
int(input('Digite mais um: ')),
int(input('Digite o último valor: ')))
print(f'Você digitou os valores {listagem}')
print(f'O número nove apareceu {listagem.count(9)} vezes')
if 3 in listagem:
    print(f'O número 3 apareceu pela primeira vez na {listagem.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in listagem:
    if n % 2 == 0:
        print(n, end=' ')
