num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print('O numero {} é maior que o {}'.format(num1, num2))
elif num1 < num2:
    print('O numero {} é maior que o {}'.format(num2, num1))
else:
    print('Não existe valor maior, os numeros são iguais')