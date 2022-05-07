import random
from time import sleep
cm = str(input('Ei cara! to pensando em um numero. \nQuer tentar adivinhar? ')).strip().lower()
if cm == 'sim':
    print('Certo. O numero que estou pensando esta entre 0 e 5.')
    na = (random.randint(0, 5))
    cm1 = int(input('qual é o numero? '))
    print('PROCESSANDO...')
    sleep(2)
    if cm1 == na:
        print('Parabens, você acertou! E está de wall.')
    else:
        print('Você errou!\n O numero que pensei foi o {}'.format(na))
else:
    print('Tudo bem, otima noite!')