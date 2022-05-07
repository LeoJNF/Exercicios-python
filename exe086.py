lista = [[], []]
for n in range(0, 7):
    numeros = int(input(f'Digite o {n}º valor: '))
    if numeros % 2 == 0:
        lista[0].append(numeros)
    else:
        lista[1].append(numeros)
print('Dos numeros digitad...')
print(f'Os pares são {sorted(lista[0])}')
print(f'Os imapres são {sorted(lista[1])}')


