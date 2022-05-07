num = int(input('escolha o primeiro termo: '))
razao = int(input('escolha a razão: '))
termo = num
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
