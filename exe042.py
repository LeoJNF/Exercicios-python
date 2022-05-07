from datetime import date
nasc = int(input('Para saber sua categoria de competição digite seu ano de nascimento:'))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Você tem {}, a sua categoria de competição é Mirim.'.format(idade))
elif idade <= 14:
    print('Você tem {}, a sua categoria de competição é Infantil.'.format(idade))
elif idade <= 19:
    print('Você tem {}, a sua categoria de competição é Junior.'.format(idade))
elif idade <= 20:
    print('Você tem {}, a sua categoria de comptição é Sênior.'.format(idade))
else:
    print('Você tem {}, a sua categoria de competição é Master.'.format(idade))
