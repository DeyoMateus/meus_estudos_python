''' Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros 
termos da progressão usando a estrutura while.'''

print("Gerador de PA")
print("<=>" * 10)
num = int(input("Digite um número: "))
ra = int(input("Digite a razão desejada: "))
ter = num
c = 1
while c <= 10:
    print("{} ".format(ter), end="")
    print(" => ", end="")
    ter += ra
    c += 1
print("Fim")

