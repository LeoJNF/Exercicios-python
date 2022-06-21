num = int(input('Digite um numero: '))
total2 = 0
total2 = sum([total2+1 for c in range(1, num+1) if num % c == 0])
print('o numero {} foi divisivel {} vezes.'.format(num, total))
if total == 2:
    print('E por isso ele é um numero primo.')
else:
    print('E por isso ele não é um numero primo.')
