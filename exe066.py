dagain = 's'
soma = media = total = maior = menor = 0
while dagain == 's':
    num = int(input('Digite um numero: '))
    dagain = str(input('Você quer continuar?[S/N] ')).lower().strip()
    soma += num
    total += 1
    media = soma/total
    if num == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você digitou {} numeros, a média entre eles é {}, a soma é {},'.format(total, media, soma))
print('o maior numero digitado foi {} e o menor foi {}'.format(maior, menor))