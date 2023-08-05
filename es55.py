'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

for pess in range(1, 6):
    pe = float(input("Digite o peso da {}ª pessoa: ".format(pess)))
ma = max(pe)
mi = min(pe)

print(ma, mi)