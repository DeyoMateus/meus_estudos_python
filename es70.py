'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

print("LISTA DE COMPRAS")
totalc = ct = tmaior = menor = 0
bt = ""
while True:
    pd = str(input("Digite o nome: "))
    pre = float(input("Digite o preço: R$ "))
    totalc += pre
    ct += 1
    if pre > 1000:
        tmaior += 1
    if ct == 1 or pre < menor:
        menor = pre
        bt = pd
    des = " "
    while des  not in "NS":
        des = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
    if des == "N":
        break
print(f"O total da compra é R${totalc:.2f}")
print(f"Quantidade de produtos {tmaior} com preço superior a R$1000,00")
print(f"O produto mais barato é o {bt} no valor de R${menor:.2f}")

