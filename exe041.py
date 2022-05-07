nota1 = float(input('nota do 1ºbimestre: '))
nota2 = float(input('nota do 2ºbimestre: '))
nota3 = float(input('nota do 3ºbimestre: '))
nota4 = float(input('nota do 4ºbimestre: '))
media = (nota1 + nota2 + nota3 + nota4)/4
if media >= 7:
    print('\033[34mParabéns, você foi aprovado! Sua media foi {:.1f}.'.format(media))
elif media < 5:
    print('\033[31mVocê foi reprovado, sua média foi {:.1f}.'.format(media))
else:
    print('\033[33mVocê está de recuperação, sua média foi {:.1f}.'.format(media))
