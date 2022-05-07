print('_'*30)
print(' '*10, 'TABUADA')
print('_'*30)
while True:
    mult = 0
    n = int(input('Digite um numero para saber sua tabuada: '))
    print('_'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {c*n}')
    print('_'*30)
print('Calculadora finalizada')