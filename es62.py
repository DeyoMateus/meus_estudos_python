'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print("Gerador de PA")
num = int(input("Digite o primeiro termo: "))
ra = int(input("Digite qual é a razão: "))
print("<=>" * 10)
ter = num
c = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print("{}".format(ter),end="")
        print(" => ", end="")
        ter += ra
        c += 1
    print("Pause")
    mais = int(input("Deseja ver mais quantos termos? "))
    print("<=>" * 10)

print("Fim de program, foram gerados {} termos da PA {}".format(total, num))