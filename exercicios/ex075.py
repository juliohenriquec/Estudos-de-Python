num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))
num3 = int(input("digite um numero: "))
num4 = int(input("digite um numero: "))


numeros = (num1, num2, num3, num4)


print(f"O número 9 apareceu {numeros.count(9)}ª vezes")
print(f"O número 3 aparece pela primeira vez na {numeros.index(3)+1}ª posição")


if (num1%2) == 0:
    print(f"O número {num1} é par")

if (num2%2) == 0:
    print(f"O número {num2} é par")

if (num3%2) == 0:
    print(f"O número {num3} é par")

if (num4%2) == 0:
    print(f"O número {num4} é par")