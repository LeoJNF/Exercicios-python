from datetime import date
atual = date.today().year
nasc = int(input('Quando foi seu ano de nascimento? '))
idade = atual - nasc
if idade == 18:
    print('Esta na hora de você se alistar, você tem 18 anos.')
elif idade < 18:
    falta = 18 - idade
    ano = falta + atual
    print('Você não precisa se alistar, você tem {} anos, ainda falta {} anos.\n'
          'Seu ano de alistamento é em {}'.format(idade, falta, ano))
elif idade > 18:
    passou = idade - 18
    ano = atual - passou
    print('Você já devia ter se alistado, você tem {} anos, devia ter se ha {} anos atrás.\n'
          'Seu ano de alistamento foi em {}'.format(idade, passou, ano))
