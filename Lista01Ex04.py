'''
Escreva um programa que armazene um valor de entrada em uma variável A e outro em uma variável
B. A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que
o valor que está em A passe para B e vice-versa. Ao final escrever os valores que ficaram armazenados
nas variáveis.
'''

a = int(input('Valor 1 >> '))
b = int(input('Valor 2 >> '))
print(f'a = {a} e b = {b}')
'''
x = a
a = b
b = x
'''
#ou
a, b = b, a
print(f'a = {a} e b = {b}')
