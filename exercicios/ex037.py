num = int(input('Digite um número inteiro:'))
print('Escolha a base de conversão:\n [1] para binário\n [2] para octal\n [3] para hexadecimal ')
base = int(input('Sua opção: '))
if base == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif base == 2:
    print(f'{num} em octal é {oct(num)[2:]}')
elif base == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção INVÁLIDA')
