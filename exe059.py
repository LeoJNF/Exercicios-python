from random import randint
computador = randint(0, 10)
jogador = ''
cont = 0
while jogador != computador:
    jogador = int(input('Em qual numero estou pensando? '))
    if jogador == computador:
        print('Você acertou!!', end=' ')
    elif jogador < computador:
        print('O numero que estou pensando é MAIOR!')
    elif jogador > computador:
        print('O numero que estou pensando é MENOR!')
    cont += 1
print('E precisou de {} tentativas.'.format(cont))