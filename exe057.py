cont = 0
idadet = 0
maior = 0
nomev = ''
for p in range(1, 5):
    print('-'*5, '{}º PESSOA'.format(p), '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('idade: '))
    sexo = str(input('Sexo (M/F): ')).lower()
    idadet += idade
    if sexo == 'f' and idade < 20:
        cont += 1
    if idade > maior and sexo == 'm':
        maior = idade
        nomev = nome
print('A média de idade do grupo é de {}'.format(idadet/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, nomev))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
