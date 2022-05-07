from random import randint
jogos = []
print('='*30)
print('       JOGOS MEGA SENA')
print('='*30)
qntd = int(input('Quantos jogos você quer? '))
for c in range(0, qntd):
    for n in range(0, 6):
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
        elif num in jogos:
            num = randint(1, 60)
            jogos.append(num)
    print(f'jogo {c+1}: {sorted(jogos)} ')
    jogos.clear()

