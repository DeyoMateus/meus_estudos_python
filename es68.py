'''Faça um programa que jogue par ou ímpar com o computador de 0 a 20. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
c = 0
print("-" * 50)
print("Vamos jogar Ímpar ou Par?")
print("-" * 50)
while True:
    jg = str(input("Qual você escolhe [I/P]? ")).strip().upper()[0]
    jgd = int(input("Escolha um número: "))
    if jgd > 20:
        break
    pc = randint(1,20)
    v = (pc + jgd) % 2
    if v == 0 :
        r = "P"
    else:
        r = "I"
    if jg == r:
        print(f"Você VENCEU escolheu {jg} e número {jgd} e o PC {pc} P")
        c += 1
    else:
        print(f"Você perdeu o PC escoleheu {r} e número {pc}, vc escolheu {jg} e número {jgd}")
        print(f"O jogador venceu {c} rodadas consecutivas")
        break
print("Fim de jogo")
        
    
