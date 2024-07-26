valores =  []
while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja adicionar outro número?[S/N]: ')).upper()
    if continuar == 'N':
        break

print(valores.sort)