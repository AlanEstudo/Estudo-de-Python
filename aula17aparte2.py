# Variáveis Compostas (Listas) Parte 2
#dados = []
#dados.append('Pedro')
#dados.append(25)
#pessoas = []
#pessoas.append(dados[:])

pessoas = [['Pedro', '25'], ['Maria', '19'], ['João', '32']]
#print(pessoas[0][0])
#print(pessoas[1][1])
#print(pessoas[2][0])
#print(pessoas[1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')