lista = []
listap = []
listai = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = input('Quer continuar? [S/N]').upper()
    while cont != 'N' and cont != 'S':
        cont = input('Digite uma opção correta. [S/N]').upper()
    if cont == 'N':
        break
for n in lista:
    if n % 2 == 0:
        listap.append(n)
    if n % 2 == 1:
        listai.append(n)
print(f'Você escolheu esses numeros: {lista}')
print(f'Desses numeros, esses são pares: {listap}')
print(f'E esses são impares? {listai}')
