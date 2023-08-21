'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

lista = ("Farinha", 4.0,
        "Ovos", 0.90,
        "Arroz", 23.90,
        "Jeião", 6,
        "Macarrão", 5)
print("="*30)
print(f"{'LISTA DE COMPRAS':^30}")
print("="*30)

for l in range(len(lista)):
    if l % 2 == 0:
        print(f"{lista[l]:.<30}", end="")
    else:
        print(f"R${lista[l]:>6.2f}")
print("="*30)


