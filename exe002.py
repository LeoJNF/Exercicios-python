from titulo import titulo

numeros = list()
pares = list()
impares = list()
titulo('Dados aleátorios sobre inteiro')
for n in range(5):
    numeros.append(int(input(f'Digite o {n+1}º valor: ')))
print('Numeros pares identificados: ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
        pares.append(n)
    else:
        impares.append(n)
print(f'\nA soma dos numeros par: {sum(pares)}')
print('Numeros impares identificados: ')
for n in impares:
    print(n, end=' ')
