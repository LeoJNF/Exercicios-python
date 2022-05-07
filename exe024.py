num = int(input('digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('a unidade do numero {} é {}.'.format(num, u))
print('a dezena do numero {} é {}.'.format(num, d))
print('a centena do numero {} é {}.'.format(num, c))
print('o milhar do numero {} é {}.'.format(num, m))


