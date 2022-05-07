from random import randint


def sorteia(lista):
    print('Cinco valores aleatórios: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valors pares de {lista}, temos {soma}')


numero = list()
sorteia(numero)
somapar(numero)