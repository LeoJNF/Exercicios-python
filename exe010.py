from time import sleep
print('-' * 10, 'TABUADA', '-' * 10)
num = int(input('Qual tabuada você quer saber: '))
print('PROCESSANDO...')
sleep(3)
print('-' * 20)
print('\033[31m{} x {} = {}'.format(num, 1, num * 1))
print('{} x {} = {}'.format(num, 2, num * 2))
print('{} x {} = {}'.format(num, 3, num * 3))
print('{} x {} = {}'.format(num, 4, num * 4))
print('{} x {} = {}'.format(num, 5, num * 5))
print('{} x {} = {}'.format(num, 6, num * 6))
print('{} x {} = {}'.format(num, 7, num * 7))
print('{} x {} = {}'.format(num, 8, num * 8))
print('{} x {} = {}'.format(num, 9, num * 9))
print('{} x {} = {}\033[m'.format(num, 10, num * 10))
print('-' * 20)




