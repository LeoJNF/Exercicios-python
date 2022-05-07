import random
n = maior = 0
menor = 0
print('Os numeros sorteados foram: ', end='')
while n < 5:
    nums = random.randint(1, 10)
    numeros = nums
    n += 1
    print(numeros, end=' ')
    if n == 1:
        maior = nums
        menor = nums
    else:
        if nums > maior:
            maior = nums
        if nums < menor:
            menor = nums
print(f'\nO menor valor sorteado foi {menor} \no maior valor sorteado foi {maior}')