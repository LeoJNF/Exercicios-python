print('\033[7m*' * 10, 'CALCULADORA DE BASE', '**********\033[m')
numero = int(input('\033[31mEscolha um numero para converter: '))
tipo = int(input('Qual a base? 1 para binario, 2 para octal e 3 para hexadecimal: '))
if tipo == 1:
    print('\033[31mO numero {} em binário é equivalente a {}'.format(numero, bin(numero)[2:]))
elif tipo == 2:
    print('\033[34mO numero {} em octal é equivalebte a {}'.format(numero, oct(numero)[2:]))
else:
    print('\033[33mO numero {} em hexadecimal é equivalente a {}'.format(numero, hex(numero)[2:]))
