'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final 
quantos palpites foram necessários para vencer.'''

from random import randint
print("Estou pensando em um número de 0 a 10")
print("será que você consegue adivinhar qual é?")
pc = randint(0,10)
acertou = False
pa = 0
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    pa += 1 
    if jogador == pc:
        acertou = True        
    else:
        if jogador > pc:
            print("Menos... Qual seu palpite? ")
        elif jogador < pc:
            print("Mais... Qual seu papite?") 

print("Acertou depois de {} tentativas".format(pa))
