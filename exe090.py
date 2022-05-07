alunos = []
alunos1 = [[], []]
soma = cont = 0
while True:
    alunos.append(str(input('nome: ')).strip())
    cont += 1
    alunos.append(float(input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    media = (alunos[1]+alunos[2])/2
    alunos1[0].append(alunos[:])
    alunos1[1].append(media)
    alunos.clear()
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar in 'N':
        break
print('-='*30)
print('No. NOME      MÉDIA')
print('-'*50)
for n in range(0, cont):
    print(f'{n}{alunos1[0][n][0]:^12}{alunos1[1][n]:>5}')
print('-'*50)
while True:
    x = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if x >= 0:
        if x == 999:
            break
        if x > cont-1:
            x = int(input(f'A posição {x} não existe, escolha uma existente. (999 interrompe):'))
            while x > cont-1:
                x = int(input(f'A posição {x} não existe, escolha uma existente. (999 interrompe):'))
        print(f'Notas de {alunos1[0][x][0]} são {alunos1[0][x][1]} {alunos1[0][x][2]} ')
    print('-' * 50)
