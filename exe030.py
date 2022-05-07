vel = int(input('Qual a velocidade que ele está? '))
if vel > 80:
    print('você esta a {}Km, por esta acima da velocida. Voce vai ser multado.'.format(vel))
    ma = vel - 80
    print('O valor a pagar é de R${}'.format(ma * 7))
else:
    print('Parabens! Voce esta dentro da velocidade permitida')