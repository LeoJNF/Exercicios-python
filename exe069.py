from random import randint, choice
print('-='*20)
print('PAR OU IMPAR')
print('-='*20)
cont = 0
while True:
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nc = choice(lista)
    print(nc)
    nj = int(input('Escolha um valor: '))
    pi = str(input('Par ou Impar? [P/I] '))
    n = nc + nj
    if n % 2 == 0:
        ip = 'par'
    else:
        ip = 'impar'
    print('-' * 40)
    print(f'você jogou {nj} e computador {nc}. Total foi {nj+nc}, {ip}')
    print('-' * 40)
    if pi == 'p' and ip == 'par' or pi == 'i' and ip == 'impar':
        print('Você venceu. Vamos jogar denovo')
        print('-=' * 20)
        cont += 1
    else:
        break
print(f'Eu GANHEI hahahaha!! Você conseguiu ganhar {cont} vezes')