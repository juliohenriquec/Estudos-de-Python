from math import hypot
co = int(input('Comprimento do cateto oposto: '))
ca = int(input('Comprimento do cateto adjacente: '))
hip = hypot(co, ca)
print(f'A hipotenusa desse triângulo vale {hip: .2f}')
