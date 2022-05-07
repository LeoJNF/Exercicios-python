b = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 7.00)
a = '.'*20
print('-'*37)
print(f'{"LISTA DE PREÇO":^37}')
print('-'*37)
for pos in range(0, len(b)):
    if pos % 2 == 0:
        print(f'{b[pos]:.<30}', end='')
    else:
        print(f'R${b[pos]:>5.2f}')
