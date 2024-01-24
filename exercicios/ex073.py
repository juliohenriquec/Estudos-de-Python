#tupla com o nome dos pilotos
pilotos = ("M. Verstapen", "S. Perez", "L. Hamilton", "F. Alonso", "C. Leclerc", "L. Noirris", "C. Sainz Jr.", "G. Russell", "O. Piastri",
"L. Stroll", "P. Gasly", "E. Ocon", "A. Albon", "Y. Tsunoda", "V. Bottas", "N. Hulkenberg", "D. Ricciardo", "G. Zhou", "K. Magnussen",
"L. Lawson")
#achando a posição do Albon
Albon = pilotos.index("A. Albon")

print('-=' *30 )
print(f'Lista de Pilotos: {pilotos}')
print('-=' *30 )
print(f"Os 5 primeiros colocados são: {pilotos [0:5]}")
print('-=' *30 )
print(f"Os 4 ultimos colocados são: {pilotos[-4:]}")
print('-=' *30 )
print(f"Os nome dos pilitos em ordem alfabética fica: {sorted(pilotos)}")
print('-=' *30 )
print(f"A. Albon está na {Albon+1}ª posição")
print('-=' *30 )


