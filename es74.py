'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''


from random import randint
numero = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print("São os 5 números sorteados:", end=" ")  
for n in numero:
    print(n, end=" ")
print(f"\nO manior número é {max(numero)}")
print(f"O menor número é {min(numero)}")

