# Crie um programa onde o usúario digite uma prexpressão qualquer que use parêntese.
# Seu programa deverá analisar se a expressão passa está com  os parênteses abertos e fechados na ordem correta.

expre = str(input('Digite a expressão: '))
pilha = []

for parenteses in expre:
    if parenteses == '(':
        pilha.append('(')
    elif parenteses == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
