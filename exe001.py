from time import sleep

totalp = 0
so = {'Windows Server': 0, 'Unix': 0, 'Linux': 0, 'Netware': 0, 'MacOS': 0, 'Outro': 0}
print('Escolha o melhor sistema para uso em servidor')
while True:
    print('1 - Windows Server')
    sleep(.3)
    print('2 - Unix')
    sleep(.3)
    print('3 - Linux')
    sleep(.3)
    print('4 - NetWare')
    sleep(.3)
    print('5 - Mac 0S')
    sleep(.3)
    print('6 - Outro')
    perg = int(input('Pressione [1][2][3][4][5][6] para escolher:  '))
    if perg == 1:
        so['Windows Server'] = 1 + so['Windows Server']
    elif perg == 2:
        so['Unix'] = 1 + so['Unix']
    elif perg == 3:
        so['Linux'] = 1 + so['Linux']
    elif perg == 4:
        so['Netware'] = 1 + so['Netware']
    elif perg == 5:
        so['MacOS'] = 1 + so['MacOS']
    elif perg == 6:
        so['Outro'] = 1 + so['Outro']
    if perg == 0:
        break
    print('Pressione 0 para sair!')
print('~'*30)
print('Resultado da pesquisa')
print(f'{"Sistema Operacional":<23} {"Votos":^6} {"%"}')
print('~'*30)
for i in so.keys():
    totalp += so[i]
for i in so.keys():
    print(f"{i:<23} {so[i]:^6} {so[i]*100/totalp:.2f}%")
print('~'*30)
print(f'{"TOTAL":<23} {totalp:^6}')
