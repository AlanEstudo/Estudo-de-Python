# Variáveis Compostas (Listas) Parte 2
#dados = []
#dados.append('Pedro')
#dados.append(25)
#pessoas = []
#pessoas.append(dados[:])

#pessoas = [['Pedro', '25'], ['Maria', '19'], ['João', '32']]
#print(pessoas[0][0])
#print(pessoas[1][1])
#print(pessoas[2][0])
#print(pessoas[1])
#for p in pessoas:
#    print(f'{p[0]} tem {p[1]} anos de idade.')

pessoas = []
dado = []
total_maior =totam_menor = 0

for c in range(0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])# Criar uma copia da lista dado
    dado.clear()# limpa o conteudo da lista dado

for p in pessoas:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totam_menor += 1

print(f'temos {total_maior} maiores e {totam_menor} menores de idade.')
