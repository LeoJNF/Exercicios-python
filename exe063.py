num = int(input('escolha o primeiro termo: '))
razao = int(input('escolha a razão: '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = (int(input('Quantos termos você quer mostrar a mais? ')))
print('Fim')