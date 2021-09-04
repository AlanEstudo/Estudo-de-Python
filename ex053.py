# Crie um programa que leia uma frase qualquer e difa se ela é um palindromo,
# Desconsiderando os espaços.
# ex: apos a sopa
# a torre da derrota

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # separa a frase em palavras
junto = ''.join(palavras) # junta todas as palvras tirando os atributos
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('A frase digitada não é um palindromo')



