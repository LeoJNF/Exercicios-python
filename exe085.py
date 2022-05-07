dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: kg ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Quer continuar?[S/N]').strip().upper()
    while continuar != 'S' or continuar != 'N':
        continuar = input('Quer continuar?[S/N]').strip().upper()
    if continuar in 'Nn':
        break
print('-='*30)
print(f'Ao todo foi cadastrado {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]},', end=' ')
print(f'\nO menor peso foi {menor}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]},', end=' ')





