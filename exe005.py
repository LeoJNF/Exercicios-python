listan = list()
listap = list()
listai = list()
for n in range(10):
    listan.append(int(input(f'Insira o {n+1}º valor inteiro: ')))
    if listan[n] % 2 == 0:
        listap.append(listan[n])
    else:
        listai.append(listan[n])
print(f'Lista dos numeros informados: {listan}')
print(f'Lista dos pares informados: {listap}')
print(f'Lista dos impares informados: {listai}')
