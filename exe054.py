frase = str(input('Digite um a frase: ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1 ):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não temos um palindromo')