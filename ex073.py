# Crie um tuplas preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebel, na ordem de colocação. e depois mostre:
# Apenas os 5 primeiros colocados.
# Os ultimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabetica.
# Em que posição na tabela está o time da Chapecoense

lista_Futebol_2021 = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino',
                      'Corinthians', 'Fluminense', 'Cuiabá', 'Internacional', 'Atlético-GO',
                      'Athletico-PR', 'Ceará', 'Santos', 'Juventude', 'Bahia',
                      'São Paulo', 'América-MG', 'Grêmio', 'Sport', 'Chapecoense')
print('-' * 30)
print('Os 5 primeiros colocados : ')
for c in range(0, 5):
    print(f'{c + 1 }º', lista_Futebol_2021[c])
print('-' * 30)
print('Os 4 ultimos colocados : ')
for c in range(16, 20):
    print(f'{c + 1 }º', lista_Futebol_2021[c])
print('-' * 30)
print('Times em ordem alfabéticas: ')
print(sorted(lista_Futebol_2021))
print('-' * 30)
print(f'Chapecoense esta na posição : {lista_Futebol_2021.index("Chapecoense")+1}º')





