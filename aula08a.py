#Utilizando Módulos

#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é iqual a {}'.format(num, math.floor(raiz)))

# import emoji
# print(emoji.emojize('Ola, Mundo :earth_americas:', use_aliases=True))

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é iqual a {:.2f}'.format(num, floor(raiz)))