sn = str(input('digite seu nome: ')).strip()
print('seu nome em maiusculo {}'.format(sn.upper()))
print('seu nome em minusculo {}'.format(sn.lower()))
print('seu nome tem {} letras'.format(len(sn)-sn.count(' ')))
d = sn.split()
print('seu primeiro nome tem {} letras'.format(len(d[0])))
