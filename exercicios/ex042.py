print('\033[1;34m='*28)
print('Analisador de triângulos 2.0')
print('='*28)

a = float(input('\033[33mSeguimento A: '))
b = float(input('Seguimento B: '))
c = float(input('Seguimento C: '))

TrianguloVerdade = (b + c > a) and (a + c > b) and (a + b > c)
equilatero = a == b == c
isosceles = a == b != c or a == c !=b or b == c != a
escaleno = a != b !=c

if TrianguloVerdade and equilatero:
    print('\033[32mSim, é possivel formar um triângulo com essas retas.\033[m')
    print('\033[32mE ele é EQUILÁTERO.\033[m')
elif TrianguloVerdade and isosceles:
    print('\033[32mSim, é possivel formar um triângulo com essas retas.\033[m')
    print('\033[32mE ele é ISÓSCELES.\033[m')
elif TrianguloVerdade and escaleno:
    print('\033[32mSim, é possivel formar um triângulo com essas retas.\033[m')
    print('\033[32mE ele é ESCALENO.\033[m')
else:
    print('\033[31mNão é possivel formar um triângulo com essas retas.\033[m')