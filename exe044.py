print('-----CALCULADORA IMC-----')
print('Para calcular seu imc preciso de alguns dados.')
peso = float(input('Quantos Kgs está pesando?'))
altura = float(input('Qual é a sua altura em metros?'))
imc = peso/(altura * altura)
if imc < 18.5:
    print('\033[36mSeu imc esta a {:.2f}Kg/m2, voce esta abaixo do seu peso ideal'.format(imc))
elif imc <= 25:
    print('\033[32mSeu imc esta a {:.2f}Kg/m2, voce esta no seu peso ideal'.format(imc))
elif imc <= 30:
    print('\033[35mSeu imc esta a {:.2f}Kg/m2, voce esta com sobrepeso'.format(imc))
elif imc <= 40:
    print('\033[33mSeu imc esta a {:.2f}Kg/m2, voce esta com obesidade'.format(imc))
else:
    print('\033[31mSeu imc esta a {:.2f}Kg/m2, voce esta com obesidade morbida'.format(imc))