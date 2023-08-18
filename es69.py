'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
print("\033[34m---\033[m"*10)
print("\033[32mCADASTRO\033[m")
print("\033[34m---\033[m"*10)
qtdh = mulherm = maior = 0
while True:
    id = int(input("Digite sua idade: "))
    sx = " "
    while sx not in "MF":
        sx = str(input("Digite seu sexo [F/M]: ")).upper().strip()[0]
    if id >= 18:
        maior +=1
    if id < 20 and sx == "F":
        mulherm += 1
    if sx == "M":
        qtdh += 1
    res = " "
    while res not in "NS":
        res = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]
    if res == "N":
        break
print("\033[34m---\033[m"*10)
print(f"Foram {maior} pessoas com mais de 18 anos.")
print("\033[34m---\033[m"*10)
print(f"Foram cadastrados {qtdh} homens.")
print("\033[34m---\033[m"*10)
print(f"Foram {mulherm} mulheres com menos de 20 anos.")
print("\033[34m---\033[m"*10)
