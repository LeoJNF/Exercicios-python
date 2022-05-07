from time import sleep
print('\033[7m-----''Seja Bem-vindo ''-----\033[m')
sleep(1)
print('Para a aprvação do empréstimo preciso de alguns dados.')
valorc = float(input('\033[36mQual é o valor da casa? R$'))
valors = float(input('Qual é o valor do seu salário? R$'))
anosp = int(input('Em quantos anos pretende pagar? '))
print('\033[34mPROCESSANDO...\033[m')
sleep(2)
print('__'*35)
parca = valorc / anosp
parcm = parca / 12
trinta = (valors * 30 / 100)
if parcm < trinta:
    print('\033[32mParabéns! Seu empréstimo foi aprovado.\n'
          'Você vai está pagando R${:.2f} por mês durante {} anos.\033[m'.format(parcm, anosp))
else:
    print('\033[31mInfelizmente o seu emprestimo excede 30% do valor do seu salario, para o pagamento mensal.'
          '\nO seu emprestimo foi negado!.\033[m')
print('--'*35)