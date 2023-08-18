'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print("\033[32m>>>>>\033[m" * 10)
print("{:^50}".format("BANCO DJ"))
print("\033[32m>>>>>\033[m" * 10)
sc = int(input("Quanto deseja sacar? R$"))
ced = 50
tced = 0
while True:
    if sc >= ced:
        sc -= ced
        tced += 1
    else:
        if tced > 0:
            print(f"Total de {tced} de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tced = 0
        if sc == 0:
            break
print("Obrigado, volte sempre!")