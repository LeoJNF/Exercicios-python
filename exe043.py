r1 = int(input('Digite um valor de uma reta: '))
r2 = int(input('Digite outro valor: '))
r3 = int(input('Digite mais um valor: '))
soma1 = r1 + r2
soma2 = r2 + r3
soma3 = r1 + r3
if r3 >= soma1 or r2 >= soma3 or r1 >= soma2:
    print('Com essas retas nao pode ser feito um triangulo.')
elif r1 == r2 == r3:
    print('Com essas retas se faz um triangulo equilatero.')
elif r1 == r2 or r2 == r3 or r3 == r1:
    print('Com esses valores se faz um triangulo isoscelos')
else:
    print('Com esses valores se faz um triangulo escaleno')