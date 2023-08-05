'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
 Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
cont = 0
for n in range(1,7):
    l = int(input("Digite um número: "))
    if l % 2 == 0:
        soma += l
        cont += 1
print("Você inceriu {} números pares e sua é {}".format(cont, soma))
