dkm = int(input('Qual vai ser a distancia da sua viagem em km?'))
if dkm >= 200:
    print('Por conta da distancia, {}km, o valor da sua viagem vai ficar R${:.2f}'.format(dkm, dkm * 0.45))
else:
    print('Por conta da distancia, {}km, o valor da sua viagem vai ficar R${:.2f}'.format(dkm, dkm * 0.50))