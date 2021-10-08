# funções
'''
def lin():
    print('-' * 30)


lin()
print(' Alan ')
lin()


def mensagem(msg):
    print('-=' * 30)
    print(msg)
    print('-=' * 30)


mensagem('Alan')
'''

''''
def soma(a, b):
    s = a + b
    print(s)


soma(2, 5)
'''

'''
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 5, 8, 10)
'''

'''
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 2]
dobra(valores)
print(valores)
'''

def soma(* valores):
    s=0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
