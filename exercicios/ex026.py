frase = str(input('Digite uma frase: ')).strip().upper()

conta = frase.count('A')
print(f'A letra A aparece na frase {conta} vezes.')

p = frase.find('A')+1
print(f'A primeira letra A aparece na posição {p}.')

u = frase.rfind('A')+1
print(f'A ultima letra A aparece na posição {u}.')




