import math
co = float(input('Qual é o cateto oposto? '))
ca = float(input('qual é o cateto adjacente? '))
h = math.hypot(co, ca)
print('Hipotenusa vale {:.2f}cm'.format(h))

