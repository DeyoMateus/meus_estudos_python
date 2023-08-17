'''Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando 
o número solicitado for negativo.'''

from time import sleep
while True:
    print("<->" * 10)
    num = int(input("Qual tabuada você deseja? "))
    if num < 0:
        break
    for c in range (1, 11):
        print(f"{num} x {c} = {num*c}")
    sleep (1)
print("Tabuada encerrada")
