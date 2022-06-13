lista = []
print('Insira quantos valor quiser!!')
print('obs. -1 para parar')
while True:
    lista.append(int(input('informe aqui --> ')))
    if -1 in lista:
        break
lista.pop(len(lista)-1)
print(f'Foi informado {len(lista)} numeros.')
print(f'Os numeros informados: {lista}')
lista.reverse()
print(f'A ordem inversa {lista}')
print(f'A soma dos valores {sum(lista)}')
print(f'A média dos valores {sum(lista)/len(lista):.2f}')
print('Numeros informados acimda da média: ', end=' ')
for n in lista:
    if n > sum(lista)/len(lista):
        print(n, end=' ')
print('\nNumeros abaixo de sete:', end=' ')
for n in lista:
    if n < 7:
        print(n, end=' ')
print('\nVALEU PAIZAO. Programa acabou!!')
