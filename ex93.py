# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# depois vai ler a quantidade de gols feitos em cada partida.
# No final tudo isso vai ser quardado em um dicionario, incluindo o total de gols feitos durante o campeonato

dados = {}
gols = []
dados["Nome"] = str(input('Nome: '))
dados["partidas"] = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, dados["partidas"]):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
dados["Gols"] = gols
dados["Total"] = sum(gols)
print('-=' * 35)
print(dados)
print('-=' * 35)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 35)
print(f'O jogador {dados["Nome"]} jogou {dados["partidas"]} partidas.')
for c in range(0, dados["partidas"]):
    print(f'  => Na partida{c+1}, fez {dados["Gols"][c]} gols.')
print(f'Foi um total de {dados["Total"]} gols.')
