frase = str(input('digite uma frase:')).lower().strip()
print('na palavra acima tem {} a.'.format(frase.count('a')))
print('aparece a pela primeira vez na {}ª letra.'.format(frase.find('a')+1))
print('aparece a pela ultima vez na {}ª letra.'.format(frase.rfind('a')+1))
