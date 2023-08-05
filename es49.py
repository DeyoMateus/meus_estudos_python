'''Mostre a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

tb = int(input("Qual a tabuada que deseja? "))
for n in range(1, 11):
    print("{} x {} = {} ".format(tb, n, tb*n))