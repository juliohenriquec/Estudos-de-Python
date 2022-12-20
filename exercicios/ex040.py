n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média foi {media}')
if media < 5:
    print('\033[31mREPROVADO\033[m')
elif 7 > media >= 5:
    print('\033[33mRECUPERAÇÃO\033[m')
elif media >= 7:
    print('\033[32mAPROVADO\033[m')
