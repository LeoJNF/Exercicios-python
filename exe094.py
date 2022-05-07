jfutebol = {}
gols = []
c = 0
jfutebol['nome'] = str(input('Qual é o nome do jogador? '))
jfutebol['partidas'] = int(input('Quantas partidas ele jogou? '))
for g in range(0, jfutebol['partidas']):
    gols.append(int(input(f'Quantos gols ele fez na {g+1}º partida? ')))
    c += gols[g]
jfutebol['gols'] = gols
jfutebol['total'] = c
print('-='* 30)
print(f'O campo nome tem o valor {jfutebol["nome"]}')
print(f'O campo gols tem o valor {jfutebol["gols"]}')
print(f'O campo total tem o valor {jfutebol["total"]}')
print('-='* 30)
print(f'O jogador {jfutebol["nome"]} jogou {jfutebol["partidas"]} partidas.')
for p in range(0, jfutebol['partidas']):
    print(f'    => Na partida {p+1}, fez {gols[p]} gols')
print(f'Foi um total de {jfutebol["total"]} gols.')

