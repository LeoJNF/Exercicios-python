times = ('corinthians', 'santos', 'fluminense', 'são paulo', 'coritiba',
         'américa-MG', 'atletico-MG', 'ceara', 'cuiabá','avaí', 'bragantino',
         'flamengo', 'atletico-GO','palmeiras', 'juventude', 'goias', 'fortaleza',
         'botafogo', 'internacional', 'athletico-pr')
print('-_'*40)
print(f'Os cincos primeiro colocados em ordem são {times[0:5]}')
print('-_'*40)
print(f'Os cincos ultimos colocados em ordem são {times[15:21]}')
print('-_'*40)
print('Em ordem alfabetica', sorted(times))
print('-_-'*30)
while True:
    time = input('\nQual time você quer saber a posição? ').lower().strip()
    print(f'atualmente o {time} esta em {(times.index(time) + 1)}º lugar.')
    cont = input('Você quer saber a posição de mais times? [S/N]').upper().strip()
    while cont != 'S' and cont != 'N':
        cont = input('Digite uma opção válida. [S/N]').upper().strip()
    if cont == 'N':
        break
