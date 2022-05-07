valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor da {cont} posição: ')))
print('='*30)
print(f'Os valores digitados foi:{valores}')
maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi {maior} que está na posição', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} que está na posição', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')

