from math import cos, sin, tan, radians
x = float(input('qual é o angulo? '))
cos = cos(radians(x))
seno = sin(radians(x))
tan = tan(radians(x))
print('cosseno vale {:.2f}, o seno vale {:.2f} e a tangente vale {:.2f}'.format(cos, seno, tan))

