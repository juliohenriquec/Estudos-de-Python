import math
num = int(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print(f'O seno de {num}° é {seno:.2f}')
print(f'O cosseno de {num}° é {cos:.2f}')
print(f'A tangente de {num}° é {tan:.2f}')
