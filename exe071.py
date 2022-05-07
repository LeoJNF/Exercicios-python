print('_'*30)
print('LOJA ELTRÔNICOS ZONA LESTE')
print('_'*30)
soma = cont = totmil = barato = 0
menor = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < barato:
        barato = preco
        menor = produto
    continuar = str(input('Quer continuar?[S/N] ')).strip().upper()
    while not continuar == 'S' and not continuar == 'N':
        continuar = str(input('Quer continuar?[S/N]')).strip().upper()
    if continuar == 'N':
        break
print(f'Você teve o gasto total de R${soma:.2f}, {totmil} produtos custaram mais de R$1000.00')
print(f'e o produto mais barato foi o {menor} de valor {barato:.2f}')