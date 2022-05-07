def maior(* num):
    print('-'*30)
    print('Analisando valores informados...')
    for v in num:
        print(f'{v}', end=' ')
    print(f'Foram digitados {len(num)} numeros')
    if len(num) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(num)}.')


maior(1, 4, 6, 7, 8)
maior(4, 7, 0)
maior(1, 2)
maior()
