n = int(input('digite algo:'))
if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0 and n % 5 != 1:
    print('fIZZ')
elif n % 3 != 0 and n % 5 == 0:
    print('Buzz')
elif n % 3 != 0 and n % 5 != 0:
    print('i')