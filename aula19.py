# Variáveis Compostas (Dicionários)
pessoas = {'Nome': 'Alan', 'sexo': 'M', 'Idade': '32'}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print('=' * 30)

print(pessoas.keys())
print('=' * 30)

print(pessoas.values())
print('=' * 30)

print(pessoas.items())
print('=' * 30)

for k in pessoas.keys():
    print(k)
print('=' * 30)

for v in pessoas.values():
    print(v)
print('=' * 30)

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('=' * 30)

del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('=' * 30)

pessoas['Nome'] = 'Camila'
pessoas['peso'] = '83.8'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('=' * 30)

brasil1 = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil1.append(estado1)
brasil1.append(estado2)
print(brasil1[0]['uf'])
print('=' * 30)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()


