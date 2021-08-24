#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

vlNome = str(input('Nome: ')).strip()

vlLista = vlNome.split()

print('Nome completo: {}'.format(vlNome))
print('Primeiro nome: {}'.format(vlLista[0]))
#print('Último nome: {}'.format(vlLista.pop()))
print('ùltimo nome: {}'.format(vlLista[len(vlLista) - 1]))

