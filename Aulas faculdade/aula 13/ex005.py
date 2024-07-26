#Escreva um programa que leia o primeiro termo e a razão de uma progressão
#aritmética (PA). Mostre os 15 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print(termo)
for c in range (1, 15):
    termo += razao
    print(termo)