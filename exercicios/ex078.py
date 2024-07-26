valores = []

for c in range(0, 5): 
    valores.append(int(input('Digite um número: ')))

print(f"O menor número digitado foi {min(valores)} na {valores.index(min(valores))+1}ª posição.")
print(f"O maior número digitado foi {max(valores)} na {valores.index(max(valores))+1}ª posição.")
