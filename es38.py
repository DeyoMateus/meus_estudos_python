'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:'''

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))

if n1 > n2:
    print("\033[32mO número {:.2f} é maior que o número\033[m \033[31m{:.2f}\033[m".format(n1, n2))
elif n1 < n2:
    print("\033[32mO número {:.2f} é maior que o número\033[m \033[31m{:.2f}\033[m".format(n2, n1))
else:
    print("\033[32mO número {:.2f} é igual ao número {:.2f}\033[m".format(n1, n2))
print("\033[32mObrigado por participar!\033[m")