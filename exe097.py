def area(a, b):
    print(f'A área de um terreno {a}x{b} é de {a*b}m².')


print('Controle de Terrenos')
print('-'*30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
