sexo = str(input('Qual seu sexo?[M/F]')).lower().strip()
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Digite um sexo válido:[M/F]')).lower().strip()
print('Sexo {} registrado com sucesso'.format(sexo))
