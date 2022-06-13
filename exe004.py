print('TRIANGULOS')
tri = []

for n in range(3):
    tri.append(int(input(f'Informe o {n+1}° lado: ')))
if tri[0] + tri[1] > tri[2] and tri[1] + tri[2] > tri[0] and tri[0] + tri[2] > tri[1] :
    print('é um triangulo', end=' ')
    if tri[0] != tri[1] and tri[0] != tri[2] and tri[1] != tri[2]:
        print('Escaleno')
    elif tri[0] == tri[1] and tri[0] == tri[2]:
        print('Equilátero')
    else:
        print('Isóceles')
else:
    print('não é um triângulo')
