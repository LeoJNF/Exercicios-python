alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input('Media: '))
if alunos['media'] >= 7:
    alunos['situaçao'] = 'aprovado'
elif 5 <= alunos['media'] < 7:
    alunos['situaçao'] = 'Recuperação'
else:
    alunos['situaçao'] = 'reprovado'
print(f'O aluno {alunos["nome"]} teve a media {alunos["media"]}')
print(f'O aluno foi {alunos["situaçao"]}')

