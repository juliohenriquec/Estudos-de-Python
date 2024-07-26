valores =  []
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja adicionar outro número?[S/N]: ')).upper()
    if continuar == 'N':
        break
print(f'Foram adicionados {len(valores)} à lista')
valores.sort(reverse=True)
print(f'Os números em ordem decrescente são {valores}')
if 5 in valores:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 não faz parte da lista')
