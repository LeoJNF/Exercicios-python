num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
acabou = False
while not acabou:
    print('_-'*20)
    print('O que você deseja realizar com esses numero\n'
          '[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior numero\n'
          '[4] novos numeros\n'
          '[5] Sair do programa')
    opcao = int(input('Escolha uma opção: '))
    print('_-'*20)
    if opcao == 1:
        print('A soma do numero {} com o numero {} é igual a {}'.format(num1, num2, num1+num2))
    elif opcao == 2:
        print('A multiplicação do numero {} com o numero {} é igual a {}'.format(num1, num2, num1*num2))
    elif opcao == 3:
        if num1 > num2:
            print('O maior numero entre o {} e {} é o {}'.format(num1, num2, num1))
        elif num1 < num2:
            print('O maior numero entre o {} e {} é o {}'.format(num1, num2, num2))
        else:
            print('Os dois numeros são iguais')
    elif opcao == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        acabou = True
        print('Tenha um otimo dia!')


