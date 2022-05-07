from time import sleep


def contador(a, b, c):
    print('-------------------------------')
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    if a < b:
        print(f'Dê {a} até {b} de {c} em {c}')
        for v in range(a, b + 1):
            print(a, end=' ')
            sleep(0.5)
            a += c
            if a > b:
                break
    elif a > b:
        print(f'Dê {a} até {b} de {c} em {c}')
        for v in range(b - 1, a):
            print(a, end=' ')
            sleep(0.5)
            a -= c
            if a < b:
                break
    print('\n-------------------------------')


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de escolher a sequência')
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)