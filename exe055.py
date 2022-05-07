import datetime
cont = 0
contm = 0
hoje = datetime.date.today().year
for c in range(1, 8):
    n1 = int(input('Em que ano nasceu a {}º pessoa:'.format(c)))
    if hoje - n1 < 18:
        cont += 1
    else:
        contm += 1
print('Ao todo tivemos {} menores de idade'.format(cont))
print('E tambem tivemos {} maiores de idade.'.format(contm))






