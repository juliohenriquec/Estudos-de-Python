print('\033[1;34m='*25)
print('Analisador de triângulos.')
print('='*25)
a = float(input('\033[33mSegmento a: '))
b = float(input('Segmento b: '))
c = float(input('Segmento c: '))
if (b + c > a) and (a + c > b) and (a + b > c):
    print('\033[32mSim, é possivel formar um triângulo com essas retas.\033[m')
else:
    print('\033[31mNão é possivel formar um triângulo com essas retas.\033[m')
