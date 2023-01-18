n = soma = cont = 0
n = int(input('Digite um valor[999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um valor[999 para parar]: '))
print(f'Foram digitados {cont} números e a soma de todos eles é igual a {soma}!')
