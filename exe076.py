numeros = (int(input('Digite um valor :')),
           int(input('Digite outro valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite mais um valor:')))
print(f'O numero 9 aprece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 aparece pela primeira vez na {numeros.index(3) + 1}º poisição')
else:
    print('O numeros 3 não foi digitado.')
print('Os numeros pares são', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=', ')