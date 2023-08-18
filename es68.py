'''Faça um programa que jogue par ou ímpar com o computador de 0 a 20. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
c = 0
print("-" * 20)
print("Vamos jogar Ímpar ou Par?")
print("-" * 50)
while True:
        jgd = int(input("Escolha um número: "))
        jg = " "
        while jg not in "PI":
            jg = str(input("Qual você escolhe [I/P]? ")).strip().upper()[0]
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
                break
print("Fim de jogo")
print(f"O jogador venceu {c} rodadas")
        
    
