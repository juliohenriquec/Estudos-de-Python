#tupla de números
numeros = ("zero", "um", "dois", "três", "quatro",
            "cinco", "seis",  "sete", "oito", "nove",
            "dez", "onze", "doze", "treze", "quatorze", "quinze",
            "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

#pedindo o número para o usuário
while True:
    while True:
        cont = int(input("Digite um número de 0 a 20: "))
        if 0 <= cont <=20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {numeros[cont]}.')
    continuar = str(input('Gostaria de continuar?[S/N]: ')).upper()
    if continuar == "N":
        break
