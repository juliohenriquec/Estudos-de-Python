print('='*20)
print('Analisador de triângulos.')
print('='*20)
a = float(input('Segmento a: '))
b = float(input('Segmento b: '))
c = float(input('Segmento c: '))
if (b + c > a) and (a + c > b) and (a + b > c):
    print('Sim, é possivel formar um triângulo com essas retas')
else:
    print('Não, não é possivel formar um triângulo com essas retas')
