lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    for n in lista:
        x = lista.count(n)
        if x > 1:
            lista.remove(n)
            print('Valor duplicado! Não vou adicionar')
    continuar = input('Quer continuar? [S/N]').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Digite uma opção correta [S/N]').upper()
    if continuar == 'N':
        break
print(f'{sorted(lista)}')

