from datetime import date
dic = {}
dic['nome'] = input('Digite seu nome: ')
anos = int(input('Quando você nasceu:'))
dic['idade']= date.today().year - anos
dic['cart'] = int(input('Carteira de trabalho (0 não tem): '))
if dic['cart'] > 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salario'] = float(input('Salário: R$'))
    dic['aposentadoria'] = (35 + dic['contratação']) - anos
    print(f'O {dic["nome"]} tem {dic["idade"]} anos')
    print(f'ctps tem o valor {dic["cart"]}')
    print(f'Tem o salário de {dic["salario"]}')
    print(f'Aposentadoria com {dic["aposentadoria"]} anos')
else:
    print(f'O {dic["nome"]} tem {dic["idade"]} anos')
    print('Cpts tem o valor 0')
print(dic)