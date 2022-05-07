num = int(input('Digite um numero: '))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        total = total + 1
print('o numero {} foi divisivel {} vezes.'.format(num, total))
if total == 2:
    print('E por isso ele é um numero primo.')
else:
    print('E por isso ele não é um numero primo.')

