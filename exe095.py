pessoas = {}
lista = []
soma = 0
while True:
    pessoas['nome'] = (str(input('Nome: ')))
    while True:
        pessoas['sexo']= str(input('Sexo: [M/F]')).upper().strip()
        if pessoas['sexo'] in 'MF':
            break
        print('Digite uma opção correta M ou F.')
    pessoas['idade'] = (int(input('Idade: ')))
    soma += pessoas["idade"]
    lista.append(pessoas.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-='*30)
print(f'- Foram cadastrado {len(lista)} pessoas')
print(f'- A média da idade é {soma/len(lista):.2f}')
print('- As mulheres cadastradas foram: ', end=' ')
for i in range(0, len(lista)):
    if lista[i]['sexo'] == 'F':
        print(f'{lista[i]["nome"]}', end=' ')
print('\n- Lista das pessoas que estão acima da média: ')
for i in range(0, len(lista)):
    if lista[i]['idade'] > soma/len(lista):
        print(lista[i])
