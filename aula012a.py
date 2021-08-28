# Condiçoes aninhadas
# if elif else

nome = str(input('Qual é seu nome? '))
if nome == 'Alan':
    print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Camila':
    print('Belo nome feminino!')
else:
    print('Seu nome é normal.')
print('tenha um bom dia, {}'.format(nome))
