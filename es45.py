#jogar Jokenpô
from time import sleep
from random import randint
print('''
[0] Pedra
[1] Papel
[2] Tesoura''')
itens = ("Pedra", "Papel", "Tesoura")
op = int(input("Qual opção você escolhe? "))
Computador = randint(0, 2)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
print("-="*20)
print("O computador escolheu {}.".format(itens[Computador]))
print("O jogador escolheu {}.".format(itens[op]))
print("-="*20)
if op == 0 and Computador == 1:
    print("O Computador venceu!!!")
elif op == 0 and Computador == 2:
    print("O Jogador Venceu")
elif op == 1 and Computador == 0:
    print("^O Jogador venceu")
elif op == 1 and Computador == 2:
    print("O Computador venceu")
elif op == 2 and Computador == 1:
    print("O Computador venceu")
elif op == 2 and Computador == 0:
    print("O Jogador venceu")
elif op == Computador:
    print("Empate jogue novamente")
else:
    print("Valor indisponível tente novamente")
    