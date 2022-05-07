salario = float(input('Qual é o seu salario? R$'))
if salario > 1250:
   novo = (salario * 10 / 100) + salario
   resto = novo - salario
else:
    novo = (salario * 15 / 100) + salario
    resto = novo - salario
print('Parabens voce teve um aumento de R${:.2f}.\nSeu novo salario é R${:.2f}'.format(resto, novo))

