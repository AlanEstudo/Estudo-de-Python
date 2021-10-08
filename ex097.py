# Faça um programa que tenha uma função chamada escreva().
# Que receba um texto qualquer como parametro e mostre uma mensagem com tamando adaptavel

def escreva(frase):
    tam = len(frase) + 2
    print(f'-' * tam)
    print(f' {frase}')
    print(f'-' * tam)

# programa principal
texto = str(input('Digite um texto: '))
escreva(texto)
