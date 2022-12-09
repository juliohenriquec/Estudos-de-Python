from random import shuffle
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))
ordem = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem)
print(f'A ordem de apresentação será... {ordem}')
