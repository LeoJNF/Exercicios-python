num = int(input('escolha o primeiro termo: '))
num2 = int(input('escolha a razão: '))
decimo = num + (10-1) * num2
for c in range(num, decimo + num2, num2):
    print('{}'.format(c), end='-')
