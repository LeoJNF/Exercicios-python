print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
termos = int(input('Quantos termos você quer vê? '))
f1 = 1
f2 = 1
fim = 4
print('0 - 1 - 1 - ', end='')
while fim <= termos:
    fn = f1 + f2
    fim += 1
    f2 = f1
    f1 = fn
    print(fn, '- ', end='')
print('Fim')