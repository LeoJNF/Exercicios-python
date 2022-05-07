from math import factorial
n = int(input('Digite um numero para saber seu fatorial: '))
c = n
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(factorial(n)))
