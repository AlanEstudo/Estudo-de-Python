# Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final, mostra um boletim contendo a média de cada um e permita que o usúario possa mostrar as notas de cada aluno individualmente.

class_aluno = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    class_aluno.append([nome, [nota1, nota2], media])
    sair = str(input('Quer continuar? [S/N]'))
    if sair in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for indice, aluno in enumerate(class_aluno):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(class_aluno):
        print(f'Notas de {class_aluno[opc][0]} são {class_aluno[opc][1]}')
print('<<< VOLTE SEMPRE >>>')