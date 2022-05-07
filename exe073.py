numextenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
              'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
              'doze', 'treze', 'cartoze', 'quinze', 'dezesseis',
              'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Você digitou o numero {numextenso[num]}.')
    cont = input('Você quer continuar? [S/N]').strip().upper()
    if cont != 'S' and cont != 'N':
        cont = input('Escolha uma opção válida. [S/N]').strip().upper()
    if cont == 'N':
        break
print('Até logo!')

