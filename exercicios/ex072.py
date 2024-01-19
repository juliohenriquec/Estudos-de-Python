#tupla de números
numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis",  "sete", "oito", "nove",
"dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

#pedindo o número para o usuário
cont = int(input("Digite um número de 0 a 20: "))
#verificando se o usuário digitou um número entre 0 e 20
while not 0 <= cont <=20:
    #caso o usuário digite um número não compativel:
    cont = int(input("ERRO!Digite um número de 0 a 20: "))
#mostrando o número por extenso
if 0 <= cont <=20:
    print(f'{cont} por extenso é {numeros[cont]}')
