lista = ('aprender', 'jogar', 'brincar', 'massa', 'horario', 'bairro', 'gato', 'rato')
for palavras in lista:
    print(f'\nna palavra {palavras.upper()} temos ', end='')
    for vogal in palavras:
        if vogal in 'aeiou':
            print(vogal, end=' ')

