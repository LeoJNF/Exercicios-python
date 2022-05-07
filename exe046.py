from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Escolha\n[0] PARA PEDRA\n[1] PARA PAPEL\n[2] PARA TESOURA\nQual é sua escolha? '))
print('\033[34m-_-'*20)
print('\033[34mcomputador jogou {}'.format(itens[computador]))
print('\033[33mjogador jogou {}'.format(itens[jogador]))
print('-_-'*20)
if computador == 0:
    if jogador == 0:
        print('\033[37mEMPATOU')
    elif jogador == 1:
        print('\033[32mO jogador GANHOU!!')
    elif jogador == 2:
        print('\033[31mO computador GANHOU!!')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('\033[31m0 computador GANHOU!!')
    elif jogador == 1:
        print('\033[37mEMPATOU')
    elif jogador == 2:
        print('\033[32mO jogador GANHOU!!')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('\033[32mJogador GANHOU!!')
    elif jogador == 1:
        print('\033[31mO computador GANHOU!!')
    elif jogador == 2:
        print('\033[37mEMPATOU')
    else:
        print('JOGADA INVALIDA')
