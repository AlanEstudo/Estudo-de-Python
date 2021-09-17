# Crie um programa que tenha uma tuplas de várias palavras.
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

lista_palavras =('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
                 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
                 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in lista_palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='')