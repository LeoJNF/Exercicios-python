from time import sleep
print('CALCULADORA DE PREÇO')
valorp = float(input('Qual é o valor do produto? '))
print('Existe 4 opções de pagamento.')
sleep(1.5)
print('Opção 1 à vista no dinheiro ou cheque com 10% de desconto,')
sleep(1.5)
print('Opção 2 à vista no cartão com 5% de desconto,')
sleep(1.5)
print('opção 3 em 2x no cartão sem juros,')
sleep(1.5)
print('opção 4 em 3x ou mais com 20% de juros.')
sleep(1.5)
opcao = int(input('qual opção voce escolhe, 1, 2, 3 ou 4? '))
if opcao == 1:
      desc1= valorp - (valorp * 10 / 100)
      print('Opção de pagamento escolhida foi a vista dinheiro ou cheque com 10% de desconto. '
            'Valor total a pagar R${:.2f}'.format(desc1))
elif opcao == 2:
      desc2 = valorp - (valorp * 5 / 100)
      print('Opção de pagamento escolhida foi a vista no cartao com 5% de desconto. '
            'Valor total a pagar R${:.2f}.' .format(desc2))
elif opcao == 3:
      parc2 = valorp / 2
      print('Opção de pagamento escolhida foi em 2x no cartao. Valor de cada parcela é R${:.2f} '
            'de Valor total a pagar é de R${:.2f}.'.format(parc2, valorp))
else:
      qtsx = int(input('Em quantas vezes vocês vai parcelar? '))
      juros = (valorp * 20 / 100) + valorp
      parc3 = juros / qtsx
      print('Opção de pagamento escolhida foi de {}x no cartao. Valor de cada parcela é R${} '
            'Valor total a pagar é de R${:.2f}.'.format(qtsx, parc3, juros))
