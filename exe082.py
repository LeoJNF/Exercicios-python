lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = input('Você quer digitar mais numeros? [S/N]').upper().strip()
    while cont != 'S' and cont != 'N':
        cont = input('Digite uma resposta válida. [S/N]').upper().strip()
    if cont == 'N':
        break
print(f'Foi digitado {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Em ordem decrescente {lista}.')
if 5 in lista:
    print('O 5 faz parte da lista.')
else:
    print('Não há numero 5 na lista.')