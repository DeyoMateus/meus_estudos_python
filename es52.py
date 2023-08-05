'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''


nu = int(input("Digite um número: "))
tot = 0
for p in range(1, nu + 1):
    if nu % p == 0:
        print("\033[33m", end=" ")
        tot = tot + 1
    else:
        print("\033[31m", end= " ")
    print("{}".format(p), end=" ")

print("\033[m O número {} foi divisível {} vezes".format(nu, tot))
if tot == 2:
    print("Por isso ele é primo")
else:
    print("Por isso ele não é primo")