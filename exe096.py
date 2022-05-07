jfutebol = {}
lista = []
gols = []
while True:
    total = 0
    gols.clear()
    jfutebol['nome'] = str(input('Qual é o nome do jogador? '))
    jfutebol['partidas'] = int(input('Quantas partidas ele jogou? '))
    for g in range(0, jfutebol['partidas']):
        gol = int(input(f'   Quantos gol marcou na {g+1}º partida? '))
        total += gol
        gols.append(gol)
    jfutebol['gols'] = gols.copy()
    jfutebol['total'] = total
    lista.append(jfutebol.copy())
    while True:
        continuar = str(input('Quer adicionar mais jogador? [S/N] '))
        if continuar in 'NnSs':
            break
    if continuar == 'N':
        break
print('-='*30)
print(f'{"cod":<5}{"nome":<10}{"gols":<7}{"total":>6}')
print('-'*30)
for j in range(0, len(lista)):
    print(f'{j:<5}{lista[j]["nome"]:<3}{lista[j]["gols"]}{lista[j]["total"]:>6}')
print('-'*30)
print(len(lista))
while True:
    x = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    print(f'  LEVANTAMENTO DO JOGADOR {lista[x]["nome"]}')
    if x == 999:
        break
    else:
        for g in range(0, len(lista[x]['gols'])):
            print(f'  No jogo {g+1} fez {lista[x]["gols"][g]} gols')
print('Volte sempre')
