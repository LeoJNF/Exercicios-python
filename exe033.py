ano = int(input('Digite um ano, para vê se é bissexto: '))
un = ano // 1 % 10
d = (ano // 10 % 10) * 10 + un
c = ano / 400
anob = d / 4
print('{}, {}'.format(anob, d))
if anob % 2 == 0:
    print('Este ano é bissexto.')
    if c % 2 == 0:
        print('este ano é bissexto')
else:
    print('Este ano não é bissexto')