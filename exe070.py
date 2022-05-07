cads = maior = sexom = fem20 = 0
while True:
    print('-' * 30)
    print('CADASTRO DE PESSOAS')
    print('-' * 30)
    sexo = str(input('Qual é o seu sexo[M/F]')).lower().strip()[0]
    while not sexo == 'm' and not sexo == 'f':
        sexo = str(input('Qual é o seu sexo[M/F]')).lower().strip()[0]
    idade = int(input('Qual é a sua idade? '))
    cads += 1
    if idade >= 18:
        maior += 1
    if sexo == 'm':
        sexom += 1
    if sexo == 'f' and idade < 20:
        fem20 += 1
    print('-' * 30)
    continuar = str(input('Quer continuar? [S/N]')).lower().strip()
    while not continuar == 's' and not continuar == 'n':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar == 'n':
        break
print(f'Foi cadastradado {cads} pessoas, dessas pessoas {maior} são maiores de 18 anos, {sexom} são homens')
print(f'e {fem20} são mulheres com menos de 20 anos')


