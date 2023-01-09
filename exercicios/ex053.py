frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #separei todas as palavras da frase individualmente
junto = ''.join(palavras) #juntei todas as palavras da frase para conseguir desecondiderar espaços
inverso = ''
for letra in range(len(junto)-1 , -1 , -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'{junto} invertido é {inverso} e é um Palíndromo!')
else:
    print(f'{junto} invertido é {inverso} e é não é um Palíndromo!')

