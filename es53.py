'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
 desconsiderando os espaços. Exemplos de palíndromos:'''

f = str(input("Digite uma frase: ")).strip().upper()
p = f.split()
j = ''.join(p)
i = j[:: -1]
print("O inverso de {} é {}".format(j, i))
if i == j:
    print("Temos um palíndromo")
else:
    print("Não temos um palíndromo")