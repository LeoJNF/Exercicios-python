soma = qntd = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    soma += num
    qntd += 1
print(f'Foram digitados {qntd} numeros a soma total desses numeros é {soma}')