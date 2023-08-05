'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

menor = 0
maior = 0
for pess in range(1, 6):
    pe = float(input("Digite o peso da {}ª pessoa: ".format(pess)))
    if pess == 1:
        menor = pe
        maior = pe
    else:
        if pe > maior:
            maior = pe
        if pe < menor:
            menor = pe
print("O menor peso registrado foi de {} Kg".format(menor))
print("O maior peso registrado foi de {} Kg".format(maior))