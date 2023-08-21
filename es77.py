'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavra = ("Python", "Computador", "Marmita", "Perfume", "Comida", "Perfeita", "Bemfica")

for p in palavra:
    print(f"\nNa palabra {p.upper()} temos:", end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(f"{letra}", end= " ")
